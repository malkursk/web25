from django.urls import path
from krik.views import *
urlpatterns = [
    path('',startfun),
    path('02/',funk02),
    path('calc/<str:val>', calc)
]