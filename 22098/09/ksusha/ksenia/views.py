from django.shortcuts import render, HttpResponse
from ksenia.utils import *
def startfunction (request):
    return HttpResponse ("Гончарова Ксения Дмитриевна ГУ-31б")
def func02 (request):
    return render (request,"02/index.html")
def calc (request, val):
    return HttpResponse (converter(val))
