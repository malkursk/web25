from django.shortcuts import render, HttpResponse
from WELL.utils import *

def Fell(request):
    return HttpResponse("Приветик")

def MELL(request):
    return render(request, "02/index.html")

def SELL(request):
    return render(request, "03/index.html")

def DELL(request, val):
    return HttpResponse(RELL(val))

def pagenotfound(request, exception):
    return HttpResponse("Неполучилось")
