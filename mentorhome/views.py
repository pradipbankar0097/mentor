from django.shortcuts import render, HttpResponse
from .models import Course,Trainer

courses_details = Course.objects.all()
trainers_details = Trainer.objects.all()


# Create your views here.

def index(request):
    context = {'student_count': 1203,
               'course_count': 32,
               'trainer_count': 8,
               'event_count': 50,
               }
    print(courses_details)
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def courses(request):
    return render(request, 'courses.html')


def events(request):
    return render(request, 'events.html')


def pricing(request):
    return render(request, 'pricing.html')


def trainers(request):
    context = {
        'trainers_details' : trainers_details,
    }
    print(trainers_details)
    trainers_array=[]
    print(trainers_details[0])
    return render(request, 'trainers.html', context)
