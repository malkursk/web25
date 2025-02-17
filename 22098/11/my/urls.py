
from django.urls import include, path
from .views import *

urlpatterns = [
    path('', list,name='url_list'), 
    path('create',  create, name='url_create'),  
    path('preview/<id>',  preview),       
    path('update/<id>',  update),   
    path('delete/<int:id>',  destroy),
    path('inform', about, name='url_inform'),
    path('child', gonch, name='url_child'),
    path('news', news, name='url_news'),
]