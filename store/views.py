from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.db.models.functions import Random



# Home view
def home_view (request):

    # SQL Query for the Processors
    processors= Product.objects.filter(category = 1)

    # SQL Query for the Graphics cards
    cards = Product.objects.filter(category = 2)

    # SQL Query for the Laptops
    laptops = Product.objects.filter(category = 5)

    #SQL Query for the Keyboards
    keyboards = Product.objects.filter(category = 4)

    

    return render(request, 'home.html', {
        'processors': processors,
        'cards': cards,
        'laptops': laptops,
        'keyboards': keyboards
    })

    

def components_view (request):

    products_list = Product.objects.all()
    paginator = Paginator(products_list, 32)

    page_number = request.GET.get('page')

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'components.html', {
        'products': products,
        'current_page': page_number
    })
   


def processors_view(request):

    # SQL query for get all processors and their data
    processors_list = Product.objects.filter(category = 1)

    paginator = Paginator(processors_list, 12)

    page_number = request.GET.get('page')

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'processors.html', {
        'products' : products
    })

def graphics_view (request):

    # SQL Query for get all graphis cards and their data

    cards = Product.objects.filter(category = 2)

    return render(request, 'gpu.html', {
        'products' : cards
    })

def ram_view (request):

    # SQL Query for get all ram and their data

    ram = Product.objects.filter(category = 3)

    return render(request, 'rams.html',  {
        'products': ram
    })

def motherboards_view (request):

    # SQL Query for get all motherboards ant their data
    motherboard_list = Product.objects.filter(category = 6)

    paginator = Paginator(motherboard_list,12)

    page_number = request.GET.get('page')

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'motherboards.html', {
        'products': products
    })

def storage_view (request):
    
    # SQL Query for get all SDD, M.2 ant their data
    storage_list = Product.objects.filter(category = 7)

    paginator = Paginator(storage_list,12)

    page_number = request.GET.get('page')

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'storage.html', {
        'products': products
    })

def power_view (request):

    # SQL Query for get all SDD, M.2 ant their data
    power_list = Product.objects.filter(category = 8)

    paginator = Paginator(power_list,12)

    page_number = request.GET.get('page')

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'power.html', {
        'products': products
    })

def case_view (request):

    # SQL Query for get all SDD, M.2 ant their data
    case_list = Product.objects.filter(category = 9)

    paginator = Paginator(case_list,12)

    page_number = request.GET.get('page')

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'case.html', {
        'products': products
    })

def headphones_view (request):

    # SQL Query for get all headphones and their data
    headphone_list = Product.objects.filter(category = 10)

    paginator = Paginator(headphone_list,12)

    page_number = request.GET.get('page')

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'headphones.html', {
        'products': products
    })


def keyboard_view (request):

    keyboard_list = Product.objects.filter(category = 4)

    paginator = Paginator(keyboard_list,12)

    page_number = request.GET.get('page')

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'keyboard.html', {
        'products': products
    })

def refrigeration_view (request):

    refrigeration_list = Product.objects.filter(category = 11)

    paginator = Paginator(refrigeration_list,12)

    page_number = request.GET.get('page')

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'refrigeration.html', {
        'products': products
    })

def monitor_view(request):

    monitor_list = Product.objects.filter(category = 12)

    paginator = Paginator(monitor_list,12)

    page_number = request.GET.get('page')

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'monitor.html', {
        'products': products
    })

def chair_view (request):
    
    chair_list = Product.objects.filter(category = 13)

    paginator = Paginator(chair_list,12)

    page_number = request.GET.get('page')

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'chairs.html', {
        'products': products
    })

def accesory_view (request):

    accesory_list = Product.objects.filter(category = 14)

    paginator = Paginator(accesory_list,8)

    page_number = request.GET.get('page')

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'accessories.html', {
        'products': products
    })

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

    product = get_object_or_404(Product, id=product_id)

    print(product.name)
    print(product.id)
    print(product.category)
    print(product.name)


    return render(request, 'product.html',  {
        'product': product
    })


