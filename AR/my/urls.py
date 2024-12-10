
from django.urls import include, path
from .views import *

urlpatterns = [
    path('', list, name='url_list'), 
    path('news', cards, name='url_news'), 
    path('create',  create, name='url_create'),  
    path('preview/<id>',  preview),       
    path('update/<id>',  update),   
    path('delete/<int:id>',  destroy), 
]