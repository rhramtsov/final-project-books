from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path  
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    # product - for list of products and create product.
    path('', views.index, name='homepage'),
    path('product', views.products, name="products"), 
    path('product/<id>', views.product_detail, name="product_detail"), 
    path('category', views.categories, name="categories"),    
    path('cartitems', views.cartitems, name="cartitems"),    
]