from django.shortcuts import render
from django.http import HttpResponse
from .models import Carousel

# Create your views here.
def home(request):
    obj=Carousel.objects.all()
    context={
        'obj':obj
    }
    return render(request,'base/home.html',{'navbar':'home'})

def dashboard(request):
    return render(request,'base/dashboard.html',{'navbar':'dashboard'})

def project(request):
    return render(request,'base/project.html',{'navbar','project'})
    
