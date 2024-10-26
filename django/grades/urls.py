from django.urls import path
from .views import student_grades

urlpatterns = [
    path('info/<int:student_id>/', student_grades, name='student_grades'),
]
