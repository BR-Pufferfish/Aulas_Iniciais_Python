# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 

def home(request):
    return HttpResponse("<h1>Hello World!</h1><p>Meu primeiro sistema Django está online.</p>")