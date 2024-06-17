"""
URL configuration for pc_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('components', views.components_view, name='components'),
    path('prebuilds', views.prebuilds_view, name='prebuilds'),
    path('laptops', views.laptops_view, name='laptops'),
    path('login', views.login_view, name='login'),
    path('sign_up', views.sign_up_view, name='sign_up'),
    path('log_out', views.sign_out, name='logout'),
    path('product/<int:product_id>/', views.product_view, name='product'),
    path('processors', views.processors_view, name='processors'),
    path('graphics_cards', views.graphics_view, name='graphics'),
    path('ram', views.ram_view, name='ram')


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)