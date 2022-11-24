from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def macha(request):
    return HttpResponse('<background-color:yellow><h1><marquee>WELCOME TO DARK WORLD</marquee></h1>')
def mama(request):
    return HttpResponse('<h1> django world</h1>')