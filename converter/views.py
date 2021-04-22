from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    print('working')
    return render(request,'homepage.html')