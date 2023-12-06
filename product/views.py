from rest_framework import status
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import MyUserRegistrationForm 
from .models import Category, Product
from django.contrib.auth import logout
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


@api_view(['GET', 'POST'])
def cartitems(request):
    # Replace this with real cart items (you need a model, serializer, look at products for an example)
    return Response({'cart_items': [1, 2, 3]})

@api_view(['GET', 'POST'])
def products(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        maxprice = request.GET.get('maxprice')
        category = request.GET.get('category')
        all_products = Product.objects.all()
        # Search all products that name contains the search parameter
        if search:
            all_products = all_products.filter(name__contains=search)
        # Search all products where the price is less than or equal to maxprice
        if maxprice:
            all_products = all_products.filter(price__lte=maxprice)
        if category:
            all_products = all_products.filter(category__id=category)

        all_products_json = ProductSerializer(all_products, many=True).data
        return Response(all_products_json)
    elif request.method == 'POST':
        # This line creates a serializer object from JSON data
        serializer = ProductSerializer(data=request.data)
        # This line checks the validity of JSON data
        if serializer.is_valid():
            # The serializer.save method saves a new product object
            serializer.save()
            # Returns the object that was created, including the ID
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If it's not valid, return errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id):
    # Get an object from the database by ID
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        # Create a serializer from the object
        serializer = ProductSerializer(product)
        # Return JSON using the serializer
        return Response(serializer.data)
    # PUT
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # DELETE
    elif request.method == 'DELETE':
        # product.is_active = False
        # product.save()
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view()
def categories(request):
    search = request.GET.get('search')
    all_categories = Category.objects.all()
    if search:
        all_categories = all_categories.filter(name__contains=search)
    all_categories_json = CategorySerializer(all_categories, many=True).data
    return Response(all_categories_json)

@api_view(['GET'])
def index(request):
    # Replace this with the logic for your index view
    return Response({'message': 'This is the index page'})

@api_view(['GET'])
def logout_view(request):
    logout(request)
    # Redirect to a success page, or wherever you want
    return redirect('homepage') 

@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':
        form = MyUserRegistrationForm(request.data)
        if form.is_valid():
            user = form.save()
            # No need to call user.save() again as form.save() already does this
            return Response({'message': 'Registration successful. Please log in.'}, status=201)
        else:
            return Response(form.errors, status=400)

    return Response({'message': 'Invalid request method.'}, status=405)

@api_view(['GET', 'POST'])
def contact_us(request):
    if request.method == 'GET':
        # Logic for GET request (e.g., return contact form data)
        return Response({'message': 'GET request to contact_us'})
    elif request.method == 'POST':
        # Logic for POST request (e.g., handle form submission)
        # Assuming you send data in JSON format from your React app
        contact_data = request.data
        # Process the contact_data as needed
        return Response({'message': 'POST request to contact_us received', 'data': contact_data})
    else:
        return Response({'error': 'Invalid request method'}, status=405)