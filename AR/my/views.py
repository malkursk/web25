from django.shortcuts import redirect, render
from my.forms import *
from my.models import *
from django.core import serializers
import json

def create(request):  
    if request.method == "POST":  
        form = NewsForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass
    else:  
        form = NewsForm()  
    return render(request,'my/element.html',{'form':form, 'title':'Новая запись','route': '/create'})  

def list(request): 
    return render(request,'my/list.html',{'data':News.objects.all()}) 

def cards(request): 
    return render(request,'my/cards.html',{'data':News.objects.all()}) 

def preview(request, id):
    data = serializers.serialize("json", [News.objects.get(id=id)] )[1:-1]
    data = json.loads(data)
    return render(request, 'my/element.html', {'form': data, 'title':'Просмотр, id:' + id})      

def update(request, id):
    data = News.objects.get(id=id)  
    form = NewsForm(request.POST or None, instance = data)
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'my/element.html', {'form': form, 'title':'Редактор, id:' + id,'route': '/update/'+id})  

def destroy(request, id):  
    data = News.objects.get(id=id)  
    data.delete()  
    return redirect("/")   
