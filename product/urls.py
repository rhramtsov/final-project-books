from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path  
from django.conf import settings
from django.conf.urls.static import static
from .views import logout_view



urlpatterns = [
    path('home', views.index, name='homepage'),
    path('all-books', views.products, name="all_books"), 
    path('art-books', views.products, name="art_books"), 
    path('fiction-books', views.products, name="fiction_books"), 
    path('children-books', views.products, name="children_books"), 
    path('sale', views.products, name="sale"), 
    path('product/<id>', views.product_detail, name="product_detail"), 
    path('cartitems', views.cartitems, name="cartitems"),    
    path('logout', logout_view, name='logout'),
    path('register', views.register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


