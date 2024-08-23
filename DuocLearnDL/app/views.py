from django.shortcuts import render, redirect
import requests
import json
# Create your views here.


def home(request):
    return render(request,'app/home.html')
    
    



