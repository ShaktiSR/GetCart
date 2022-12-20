from myapp.templatetags.cart import grand_total
from django.contrib.auth import models
from django.contrib.auth.models import User, auth
from django.contrib import messages
#from django.core.checks import messages
from django.http import HttpResponse, response
from razorpay.resources import payment
from myapp.models import Contect, Poll
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from .forms import CreatePollForm
from .models import Poll, product, Category, ulimiter, order
from django.urls import path
from myapp.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator
import razorpay
from polling import settings

razorpay_clint=razorpay.Client(auth=(settings.razorpay_id,
    settings.razorpay_account_id))


def searchpage(request):
    if request.method=="POST":
        searched = request.POST['searched']
        ques=product.objects.filter(tags__contains=searched)
        
        return render(request, 'searchpage.html',{'searched': searched,'ques':ques})
    else:
        return render(request, 'searchpage.html')


def mycart(request):
    ids=list(request.session.get('cart').keys())
    cartprod=product.objects.filter(id__in=ids)
    context = {}
    return render(request=request, template_name="mycart.html", context={'cartprod':cartprod})

def vote(request,poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        elif selected_option == 'option4':
            poll.option_four_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('results', poll.id)

    context = {
        'poll' : poll
    }
    return render(request, 'vote.html', context)

def paymentsummary(request):
    return render(request, 'paymentsummary.html')



def check_out(request):
    if request.method=="POST":
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        cust=request.session.get("user_id")
        #cust=request.user.username
        cart=request.session.get('cart')
        ids=list(request.session.get('cart').keys())
        cartprod=product.objects.filter(id__in=ids)

        print("ADDRESS, PHONE, CUST---------",address,phone,cust,cart,cartprod)

        #related to the payment

        #razorpay_order=razorpay_clint.order.create(dict(amount=grand_total*100, currency="INR", receipt=order.order_id, payment_capture='0' ))
        #print(razorpay_order['id'])
        #order.razorpay_order_id=razorpay_order['id']


        for pro in cartprod:
            ord= order(ord_cust=User(id=cust),
                        ord_prod=pro,
                        ord_price=pro.price,
                        ord_quant=cart.get(str(pro.id)),
                        address=address,
                        phone=phone)
                        #payment_staus=True)
            ord.placeorder()
        request.session['cart']={}
        context={}
        return render(request, 'mycart.html', context)
        #return render(request, 'paymentsummary.html',{'order':order,
        #                        'order_id':razorpay_order['id'],
        #                        'orderID':order.order_ID,
        #                        'grand_total':grand_total,
        #                        'razorpay_merchant_id':settings.razorpay_id})




    else:
        return HttpResponse("505 Not Found")
        #context = {}
        #return render(request, 'mycart.html', context)


def aboutus(request):
    return render(request, 'aboutus.html')
    #return HttpResponse("This is about page")



def home(request):
    #print("You are : ",request.session.get("user_email"))
    if request.method=="POST":
        prod_id=request.POST.get("prod_id")
        remove=request.POST.get("remove")
        cart = request.session.get('cart')
        if cart:
            quant= cart.get(prod_id)
            if quant:
                if remove:
                    if quant<=1:
                        cart.pop(prod_id)
                    else:
                        cart[prod_id]=quant-1
                else:
                    cart[prod_id]=quant+1
            else:
                cart[prod_id]=1
        else:
            cart={}
            cart[prod_id]=1
        request.session['cart']=cart
        return redirect('home')

    #request.session.clear()    #to empty the session at start of every new session
    cart=request.session.get('cart')
    if not cart:
        request.session['cart']={}
    cat_name=request.GET.get("cat_name")
    if cat_name:
        ques=product.objects.filter(category=cat_name) #prod wth cat name
        cate=Category.objects.all()
        context = {}
        return render(request=request, template_name="home.html", context={'ques':ques,'cate':cate})
    else:
        ques=product.objects.all() #set of all movies
        cate=Category.objects.all()
        context = {}
        return render(request=request, template_name="home.html", context={'ques':ques,'cate':cate})

def logout(request):
    auth.logout(request)
    return redirect('home.html')

def loginUser(request):
    #return_url=None
    #return_url=request.GET.get('returnurl')
    #print("ONE OF THE PAGE TO RETURN IS ------",return_url)
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        #check if user has entered correct pwd
        user = authenticate(username=username, password=password)
        #print("HHHHHHHHHHHHHHHHOOOOOOOOOOOME",user)
        if user is not None:
            login(request,user)
            request.session["user_id"]=user.id #giving session to user(customer)
            request.session["user_email"]=user.email #giving session to user(customer)
            #print("TWO OF THE PAGE TO RETURN IS ------",return_url)
            #if return_url:
            #    return response.HttpResponseRedirect(return_url)
            #else:
            #    return_url=None
            return redirect("home")
            # A backend authenticated the credentials
        else:
            messages.info(request,"invalid credentials")
            return redirect("login")
            


    return render(request,'login.html')


def regist(request):
    #pass1=request.POST.get('password')
    #pass2=request.POST.get('cpassword')
    if request.method=="POST":
        mail=request.POST['gmail']
        uname=request.POST['username']
        pass1=request.POST['password']
        pass2=request.POST['cpassword']
        
        if pass1==pass2:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username taken")
            elif User.objects.filter(email=mail).exists():
                messages.info(request,"email alredy exists!")
            else:
                ul=ulimiter(uid=mail,ulimit=0)
                ul.save()
                user=User.objects.create_user(username=uname,password=pass1,email=mail)
                user.save()
                messages.info(request,"user created")
                return redirect("login")
        else:
            messages.info(request,"Password not matching")
    return render(request,'regist.html')

#@method_decorator(auth_middleware)
def user_profile(request):
    cust=request.session.get('user_id')
    ord=order.get_orders_by_customer(cust)
    #print(ord)
    context = {}
    return render(request=request, template_name="user_profile.html", context={'ord':ord})


# Create your views here.
