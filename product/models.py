from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('homepage')  # Redirect to the homepage after logout


class MyUser(AbstractUser):
    def __str__(self):
        return f'{self.username}'
  
  
class Product(models.Model):
    
    category = models.ForeignKey('Category',on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100, null=False)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'

class Category(models.Model):    
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.name}'
    
  
