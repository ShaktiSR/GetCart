from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

#admin-----qwert1234@
# Create your views here.
def home(request):
    """if request.user.is_anonymous:
        return redirect("/login")
    """
    return render(request,'home.html')
    
    #return HttpResponse("This is home page")

    

def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        #check if user has entered correct pwd
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
            # A backend authenticated the credentials
        else:
            return render(request,'login.html')
            # No backend authenticated the credentials


    return render(request,'login.html')


def signin(request):
    #logout(request)
    #return redirect("/login")
    return render(request,'signin.html')