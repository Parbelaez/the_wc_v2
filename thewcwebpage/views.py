from django.shortcuts import render
from django.http import HttpResponse

def my_page(request):
    return HttpResponse("Hello World")
