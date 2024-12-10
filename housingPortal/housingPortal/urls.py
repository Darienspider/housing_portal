"""
URL configuration for housingPortal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from workers import urls
from members import urls
from workPortal import urls
from communityEvents import urls
from subscriptions import urls
from .views import * 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('members.urls'), name ='members'),  # Include members app URLs
    path('subscriptions/', include('subscriptions.urls'), name = 'subscriptions'),  # Include members app URLs
    path('workers/', include('workers.urls'), name='workers'),  # Include workers app URLs
    path('workPortal/', include('workPortal.urls'),name='workPortal'),  # Include workPortal app URLs
    path('communityEvents/', include('communityEvents.urls'), name='communityEvents'),  # Include communityEvents app URLs
    path('communityEvents/', include('communityEvents.urls'), name='communityEvents'),  # Include communityEvents app URLs
    path('communityEvents/', include('communityEvents.urls'), name='communityEvents'),  # Include communityEvents app URLs
    path('',view=home, name='home'),
    path('register/',view=register, name='register')


]
