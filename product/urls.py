from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path  
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    # product - for list of products and create product.
    path('', views.index, name='homepage'),
    path('All Books', views.products, name="all books"), 
    path('Art Books', views.products, name="art books"), 
    path('Fiction Books', views.products, name="fiction books"), 
    path('Children Books', views.products, name="children books"), 
    path('product/<id>', views.product_detail, name="product_detail"), 
    # path('category', views.categories, name="categories"),    
    path('cartitems', views.cartitems, name="cartitems"),    
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('contact_us/', views.contact_us, name='contact_us'),
    ]