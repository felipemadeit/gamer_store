from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Products

# Home view
def home_view (request):

    # SQL Query for the Processors
    products_processor = Products.objects.filter(product_category = 'Processor')

    # SQL Query for the Graphics cards
    products_cards = Products.objects.filter(product_category = 'Graphics card')

    # SQL Query for the Laptops
    products_laptops = Products.objects.filter(product_category = 'Laptops')

    # SQL Query for the Keyboards
    products_keyboards = Products.objects.filter(product_category = 'Keyboards')

    return render(request, 'home.html', {
        'processors': products_processor,
        'cards': products_cards,
        'laptops': products_laptops,
        'keyboards': products_keyboards
    })

    

def components_view (request):
    return render(request, 'components.html')


def prebuilds_view(request):
    return render(request, 'prebuilds.html')

def laptops_view (request):
    return render(request, 'laptops.html')

def login_view (request):
    if request.method == 'GET':
        return render(request, 'login.html',  {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error' : 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('home')

def sign_up_view (request):
    
    if request.method == 'GET':
        return render(request, 'sign_up.html', {
            'form' : UserCreationForm
        })
    else:
        # If the method is not get is a post method
        # Validate if the passwords match 
        if request.POST['password1'] == request.POST['password2']:
            # Try to create a user with the user data and save it
            try:
                user =  User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                # Create a session to the user registered
                login(request, user)
                # Redirect to the home view
                return redirect('home')
            # try to catch the integrity error
            # The integrity error is when the user try to sign up but he is already created
            except IntegrityError:
                return render(request, 'login.html',  {
                    'form' : UserCreationForm, 
                    'error': 'UserName Already Exists'
                })
        else:
            return render(request, 'sign_up.html', {
                'form': UserCreationForm,
                'error': 'Passwords do Not Match'
            })

def sign_out (request):
    logout(request)
    return redirect('home')


def product_view(request, product_id):
    product = get_object_or_404(Products, product_id=product_id)
    return render(request, 'product.html',  {
        'product': product
    })
