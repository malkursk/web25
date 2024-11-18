from django.urls import path
from ksenia.views import *

urlpatterns = [
    path('',startfunction),
    path('02/', func02),
    path('calc/<str:val>', calc),
    
]