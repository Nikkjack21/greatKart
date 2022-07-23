import code
from itertools import product
import json
from multiprocessing import context
from operator import itemgetter
from urllib import response
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from coupons.models import Coupons, CouponUsed
# Create your views here.

# def cart_user(request):
#     cart = request.user
#     if not cart:
#         cart = request.user.create()
#     return cart




def add_cart(request,id):   
    products    = Product.objects.get(id=id)
    cart       = Cart.objects.get(user = request.user)
    item  = CartItem.objects.filter(product=products, cart=cart)
    exists   = item.exists()
    if exists:
       
            cart_items       = CartItem.objects.get(product=products, cart=cart)
            cart_items.quantity += 1
            cart_items.save()
    else:
            cart_items          = CartItem.objects.create(
            product = products,
            quantity = 1,
            cart  = cart
        )
    cart_items.save()

    return redirect('cart')








def add_ajax_cart(request):
    if request.method == "POST":
        body = json.loads(request.body)
        id = body['id']
        
        cart_products = CartItem.objects.get(id=id)
        cart_products.quantity= cart_products.quantity+1
        cart_products.save()
        data = {'car_quantity' : cart_products.quantity }
        return JsonResponse(data)










def cart(request, total=0,quantity=0):
    cart_count  = 0
    # my_cart, created      = Cart.objects.get_or_create(user = request.user)
    my_cart =       Cart.objects.get(user=request.user)
    print(my_cart)
    print(my_cart.user_id)
    
    cart_items   = CartItem.objects.filter(cart=my_cart, is_active=True).order_by('id')
    for cart_item in cart_items:
        total += (cart_item.quantity * cart_item.product.price)
        quantity  += cart_item.quantity
    cart_count  += quantity
    tax = (2 * total) / 100
    grand_total = total + tax
       
    print(cart_items)
    context={
        "my_cart":my_cart,
        'cart_items': cart_items,
        'total': total,
        'quantity': quantity,
        'grand_total': grand_total,
        'tax': tax,
        'cart_count':cart_count,
    }
    return render(request, 'cart.html', context)


def ajax_cart(request, total=0,quantity=0):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        cart_count  = 0
        # my_cart, created      = Cart.objects.get_or_create(user = request.user)
        my_cart =       Cart.objects.get(user=request.user)
        print(my_cart)
        print(my_cart.user_id)
        
        cart_items   = CartItem.objects.filter(cart=my_cart, is_active=True).order_by('id')
        for cart_item in cart_items:
            total += (cart_item.quantity * cart_item.product.price)
            quantity  += cart_item.quantity
        cart_count  += quantity
        tax = (2 * total) / 100
        grand_total = total + tax
        
        print(cart_items)

        number = {
            "my_cart":my_cart,
            'cart_items': cart_items,
            'total': total,
            'quantity': quantity,
            'grand_total': grand_total,
            'tax': tax,
            'cart_count':cart_count,
        }
        return JsonResponse({'number': number})

    return render(request, 'cart.html')




   



def remove_cart(request,product_id):
    cart        = Cart.objects.get(user=request.user)
    products        = Product.objects.get(id=product_id)
    cart_item   = CartItem.objects.get(product=products, cart=cart)
    cart_item.delete()
    return redirect('cart')
    


def min_cart(request, id):
    products    = Product.objects.get(id=id)
    cart       = Cart.objects.get(user = request.user)
    cart_items       = CartItem.objects.get(product=products, cart=cart)
    if cart_items.quantity > 1:
        cart_items.quantity -= 1
        cart_items.save()

    return redirect('cart')




def check_out(request, total=0,quantity=0):
    my_cart =       Cart.objects.get(user=request.user)
    print(my_cart)
    print(my_cart.user_id)
    
    cart_items   = CartItem.objects.filter(cart=my_cart, is_active=True).order_by('id')
    for cart_item in cart_items:
        total += (cart_item.quantity * cart_item.product.price)
        quantity  += cart_item.quantity
    tax = (2 * total) / 100
    grand_total = total + tax
       
    print(cart_items)
    context={
        "my_cart":my_cart,
        'cart_items': cart_items,
        'total': total,
        'quantity': quantity,
        'grand_total': grand_total,
        'tax': tax,
    }
    return render(request, 'checkout.html', context)


def buy_now(request,id, total=0):
    active=1
    tax = 0
    grand_total = 0
    cart_items=0
    cart_items  = Product.objects.get(id=id)
    total += (cart_items.price * 1)
    tax  = (2 * total)/100
    grand_total = tax + total

    context ={
        'active':active,
        'cart_item': cart_items,
        'total': total,
        'tax': tax,
        'grand_total': grand_total, 

    }

    return render(request, 'checkout.html', context)




from django.contrib import messages

def apply_coupon(request, coups=None):
    if request.method == "POST":
        code = request.POST.get('coup')
        print(code  )
        try:
            coups = Coupons.objects.get(code=code)
            request.session['coupon_id'] = coups.id
            messages.success(request, 'COupon applied')
            print('Coupon verified')
            
            try:
                coupon_used = CouponUsed.objects.filter(coupon=coups,user=request.user).exists()
                if coupon_used:
                    print('Coupon already used')
                    messages.success(request, "Coupon already used")
                    return redirect(check_out)
                else:
                    coupon_used = CouponUsed.objects.create(coupon=coups, user=request.user)
                    print('Coupon created to user')
            except:
                pass
              

        except Coupons.DoesNotExist:
            print("Coupon Doesn't exist")
            return redirect(check_out)
            



    return render(request, 'checkout.html')
