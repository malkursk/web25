from django.shortcuts import render, HttpResponse
from part1.utils import *
def startfun (request):
    return HttpResponse ("Козлов Максим, гр. 44-24-229")
def func02 (request):
    return render(request, "02/index.html")
def calc (request, val):
    return HttpResponse (converter(val))
# Create your views here.
