"""
URL configuration for main project.
"""
from django.contrib import admin
from django.urls import path, include
from grades.views import student_grades, teacher_login, teacher_logout, post_grade


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('grades/', include('grades.urls')),
    path('login/', teacher_login, name='teacher_login'),
    path('logout/', teacher_logout, name='teacher_logout'),
    path('post-grade/', post_grade, name='post_grade'),    
]
