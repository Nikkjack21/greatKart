from multiprocessing import context
from unicodedata import category
from django.forms import PasswordInput
from django.http import JsonResponse
from django.shortcuts import redirect, render
from store.models import Product
from category.models import Category, MainCategory
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from cart.models import *
# Create your views here.


def index(request):
 
    # products   = Product.objects.all().filter(is_available=True)
    context ={
        # 'products': products,
        # 'category': category,
        # 'main_cat':maincat,
    }
    return render(request, 'user/index.html', context)




def signin(request):
    if request.user.is_authenticated:
        return redirect(index)
    if request.method == 'POST':
        username        = request.POST.get('username')
        pass1           = request.POST.get('password')
        user            = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            print('LOGIN SUCCESSFUL')
            cart = Cart.objects.filter(user=request.user).exists()
            print('CART USER GETTING CREATED')
            print(cart)
            if not cart:
                cart        = Cart.objects.create(user=request.user)
                cart.save()
            else:
                print('CART USER EXIST')
                cart= Cart.objects.get(user=request.user)

            data = {'username':username, "password":pass1}
            # return JsonResponse(data, safe=False)
            return redirect(index)
        print("NOT SUCCESSFUL LOGIN")
        return redirect(signin)
    return render(request, 'reg/signin.html')


def signout(request):
    logout(request)
    return redirect(index)









def main_cat_view(request,id,us=0):

    main_cate            = MainCategory.objects.get(pk=id)
    print(main_cate)
    test   =  request.GET.get('cat')
    if us == 0:
        if main_cate is not None:
            sub_cat             = Category.objects.filter(main_cat=main_cate)  
            main_prod           = Product.objects.filter(category__in=sub_cat, is_available=True)
          


        context = {
            'main_cate': main_cate.id,
            'sub_cat': sub_cat,
            'main_prod': main_prod,
        
       
            
        }

        return render(request, 'user/main_store_cat.html', context)
    else:

        sho   =  Category.objects.get(id=us)
        pros  = Product.objects.filter(category=sho)
        sub_cat             = Category.objects.filter(main_cat=main_cate)  
        main_prod           = Product.objects.filter(category__in=sub_cat, is_available=True)
        context = {
            'main_cate': main_cate.id,
            'sub_cat': sub_cat,
            'main_prod': pros,
        
        }
        return render(request, 'user/main_store_cat.html', context)

        


def store(request):
       
        main_cat = MainCategory.objects.all()
        print('THE ID IS ZERO')
        print(main_cat)
        catego  = Category.objects.all()
        products   = Product.objects.all().filter(is_available=True)
        print("STORE IS ACTUALYY WROKINGGGGGGGGGG")
        context ={
            'main_cat': main_cat,
            'products': products,
            'catego': catego
            
        }

        return render(request, 'user/store.html', context)
  


def p_store(request, id):
        print('THE ID IS NUMBER')
        main_cate            = MainCategory.objects.get(id=id)
        print(main_cate)
        categor      = Category.objects.filter(main_cat=main_cate)
        print(categor)
        productss   = Product.objects.filter(category__in=categor, is_available=True)
        print(productss)
        main_cat  = MainCategory.objects.all()
        print(main_cat)
        context ={
            'main_cat': main_cat,
            'main_cate': main_cate.id,
            'products': productss,
            'categos': categor
            
        }

        return render(request, 'user/store.html', context)






def pro_store(request, id ):
    main_cat = MainCategory.objects.all()
    category  = Category.objects.get(id=id)
    if category is not None:
        products    = Product.objects.filter(category=category, is_available=True)
        print("PRO_STORE IS ACTUALYY WROKINGGGGGGGGGG")
    else:
        products   = Product.objects.all().filter(is_available=True)
        print("EYY ITS JUST SHOWING ALL PRODUCTS")
    categ  = Category.objects.all()
    context ={
        'products': products,
        'categ': categ,
        'main_cat': main_cat,
    }

    return render(request, 'user/store_cat.html', context)


def pro_detail(request,id):
    category  = Category.objects.all()
    single_product   = Product.objects.get(id=id)

    context ={
        'category': category,
        'single_product': single_product
    }

   
    return render(request, 'user/product-detail.html', context)

def search_view(request):
    
    if request.method == 'POST':
        
        searched  = request.POST.get('search')
        if searched == '':
            print('NO SEARCH')
        else:
           
            product  = Product.objects.all().filter(product_name = searched)
            print('SEARCH SHOW')
      
        context={
            'searched': searched,
            'product': product,
            
        }

        return render(request, 'user/search.html', context)