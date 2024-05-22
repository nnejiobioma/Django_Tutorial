# from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse("Hello world: Welcome to home page")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("welcome to about page")
    return render(request, 'about.html')

def services(request):
    # return HttpResponse("This is services page")
    return render(request, 'services.html')