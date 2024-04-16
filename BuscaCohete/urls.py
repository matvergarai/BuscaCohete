"""
URL configuration for BuscaCohete project.

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
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('navigation_profiles/', views.navigation_profiles, name='navigation_profiles'),
    path('edit_navigation_profile/', views.edit_navigation_profile, name='edit_navigation_profile'),
    path('delete_navigation_profile/', views.delete_navigation_profile, name='delete_navigation_profile'),
    path('filters/', views.filters, name='filters'),
    path('history/', views.history, name='history'),
    path('stats/', views.stats, name='stats'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
]
