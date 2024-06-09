from django.shortcuts import render

# Home view
def home_view (request):
    return render(request, 'home.html')

def components_view (request):
    return render(request, 'components.html')


def prebuilds_view(request):
    return render(request, 'prebuilds.html')

def laptops_view (request):
    return render(request, 'laptops.html')

def login_view (request):
    return render(request, 'login.html')