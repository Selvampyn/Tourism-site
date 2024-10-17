from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from .models import travel

# Create your views here.

def home(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']

        obj=travel()
        obj.Username=username
        obj.Email=email
        obj.Password=password
        obj.Confirmpassword=confirmpassword
        obj.save()
    return render(request,'intex.html')