from django.shortcuts import render, HttpResponse
from krik.utils import *
def startfun (request):
    return HttpResponse ("Бобкова Кристина ГУ-31б")
def funk02 (request):
    return render (request,"02/index.html")
def calc(request, val):
    return HttpResponse(converter(val))
