

from myapp.models import product
from django import template

register = template.Library()


@register.filter(name='is_in_cart')

def is_in_cart(prod_id, cart):
    #print(prod_id, cart)
    keys=cart.keys()
    for id in keys:
        #print("ID vs ID ----",id," == ", prod_id )
        if int(id) == prod_id:
            return True
    return False



@register.filter(name='cart_count')

def cart_count(prod_id, cart):
    #print(prod_id, cart)
    keys=cart.keys()
    for id in keys:
        if int(id) == prod_id:
            return cart.get(id)
    return 0


@register.filter(name='price_total')
def price_total(prod_id, cart):
    poll = product.objects.get(id=prod_id)
    return poll.price * cart_count(prod_id,cart)


@register.filter(name='grand_total')
def grand_total(prod,cart):
    sum=0
    for p in prod:
        sum +=price_total(p.id,cart)
    return sum


@register.filter(name='multi')
def multi(num1,num2):
    return num1*num2