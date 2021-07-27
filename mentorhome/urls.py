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
    # Here we are assigning the path of our url
    path('signin', views.signIn),
    path('postsignIn/', views.postsignIn),
    path('signUp/', views.signUp, name="signup"),
    path('logout/', views.logout, name="log"),
    path('postsignUp/', views.postsignUp),
]
