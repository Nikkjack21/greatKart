from unicodedata import name
from django.urls import path
from .import views
urlpatterns = [
    path('', views.cart, name='cart'),
    # path('ajax_cart/', views.ajax_cart, name="ajax_cart"),
    path('add_cart/<int:id>/', views.add_cart, name='add_cart'),
    path('min_cart/<int:id>/', views.min_cart, name='min_cart'),
    path('delete_cart/<int:product_id>/', views.remove_cart, name='delete_cart'),
    path('checkout/', views.check_out, name='check_out'),
    path('buy_now/<int:id>/', views.buy_now, name='buy_now'),
    path('ajax_add/', views.add_ajax_cart,name="ajax_add"),
    path('coupon_apply/', views.apply_coupon, name="apply_coupon"),

    ]


    