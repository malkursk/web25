from django.shortcuts import render, HttpResponse

def pageNotFound(request, exception):
    return HttpResponse("<h1>Ошибка, такого пути не существует, будьте аккуратнее</h1>")