from django.shortcuts import render
from .models import Grade

def student_grades(request, student_id):
    grades = Grade.objects.filter(student_id=student_id)
    return render(request, 'grades/student_grades.html', {'grades': grades})
