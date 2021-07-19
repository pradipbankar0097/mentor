"""mentor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from mentorhome import views
urlpatterns = [
    path('',views.index,name='home'),
    path('about.html',views.about,name='about'),
    path('courses.html',views.courses,name='courses'),
    path('trainers.html',views.trainers,name='trainers'),
    path('contact.html',views.contact,name='contact'),
    path('pricing.html',views.pricing,name='pricing'),
    path('events.html',views.events,name='events'),
    
]
