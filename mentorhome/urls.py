from django.contrib import admin
from django.urls import path,include
from mentorhome import views

urlpatterns = [
    path('',views.index,name='home'),
    path('index.html',views.index,name='home'),
    path('about.html',views.about,name='about'),
    path('courses.html',views.courses,name='courses'),
    path('trainers.html',views.trainers,name='trainers'),
    path('contact.html',views.contact,name='contact'),
    path('pricing.html',views.pricing,name='pricing'),
    path('events.html',views.events,name='events'),
    
]
