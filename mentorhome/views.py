from django.shortcuts import render, HttpResponse
from .models import Trainer,Course
from .fireconfig import config

# for firebase

import pyrebase


# Initialising database,auth and firebase for further use
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def signIn(request):
    return render(request, "Login.html")


def home(request):
    return render(request, "Home.html")


def postsignIn(request):
    email = request.POST.get('email')
    pasw = request.POST.get('pass')
    try:
        # if there is no error then signin the user with given email and password
        user = authe.sign_in_with_email_and_password(email, pasw)
    except:
        message = "Invalid Credentials!!Please ChecK your Data"
        return render(request, "Login.html", {"message": message})
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, "Home.html", {"email": email})


def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request, "Login.html")


def signUp(request):
    return render(request, "Registration.html")


def postsignUp(request):
    email = request.POST.get('email')
    passs = request.POST.get('pass')
    name = request.POST.get('name')
    try:
        # creating a user with the given email and password
        user = authe.create_user_with_email_and_password(email, passs)
        uid = user['localId']
        idtoken = request.session['uid']
        print(uid)
    except:
        return render(request, "Registration.html")
    return render(request, "Login.html")

# end for fireabse


courses_details = Course.objects.all()
trainers_details = Trainer.objects.all()


# Create your views here.

def index(request):
    context = {'student_count': 1203,
               'course_count': 32,
               'trainer_count': 8,
               'event_count': 50,
               }
    # print(courses_details)
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def courses(request):
    context = {
        'courses_details' : courses_details,
    }
    return render(request, 'courses.html', context)


def events(request):
    return render(request, 'events.html')


def pricing(request):
    return render(request, 'pricing.html')


def trainers(request):
    context = {
        'trainers_details': trainers_details,
    }
    return render(request, 'trainers.html', context)
