from django.urls import path
from part1.views import *

urlpatterns = [
    path('', startfun),
    path('02/', func02),
    path('calc/<str:val>', calc)
]