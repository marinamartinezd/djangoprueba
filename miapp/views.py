from django.shortcuts import render
from django.http import HttpResponse

def hola(request):
    return HttpResponse("<BR>Hello world!</BR>")

def index(request):
    return render(request, 'index.html')

def acercade(request):
    return render(request, 'acercade.html')
