from unicodedata import name
from django.urls import path

from .import views
urlpatterns  = [
    path('', views.index, name='index'),
    path('signin/', views.signin,name='signin'),
    path('signout/', views.signout, name='signout'),
    path('store/', views.store, name='store'),
    path('p_store/<int:id>/', views.p_store, name='p_store'),
    path('storecat/<int:id>/', views.pro_store, name='products_by_category'),
    path('details/<int:id>/', views.pro_detail, name='details'),
    path('search/', views.search_view, name='search'),
    path('main_storecat/<int:id>/', views.main_cat_view, name='main_cat_view'),
    path('main_storecat/<int:id>/<int:us>/', views.main_cat_view, name='main_cat_view'),

    


]