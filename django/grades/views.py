from django.shortcuts import redirect, render
from .models import Grade, Teacher
from .forms import LoginForm, GradeForm
from django.contrib.auth import authenticate, login, logout

def student_grades(request, student_id):
    grades = Grade.objects.filter(student_id=student_id).select_related('subject', 'teacher')
    return render(request, 'grades/student_grades.html', {'grades': grades})


def teacher_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                teacher = Teacher.objects.get(email=email)
                # Используйте метод `check_password`, если у вас есть хэшированный пароль
                if True:  # Это предполагает, что у вас есть метод check_password
                    # login(request, teacher)
                    return redirect('student_grades', student_id=1)  # Направление на нужную страницу
            except Teacher.DoesNotExist:
                form.add_error(None, 'Неверные учетные данные')

    else:
        form = LoginForm()
    
    return render(request, 'grades/teacher_login.html', {'form': form})

def teacher_logout(request):
    logout(request)
    return redirect('teacher_login')

def post_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_grades', student_id=form.cleaned_data['student'].id)
    else:
        form = GradeForm()
    
    return render(request, 'grades/post_grade.html', {'form': form})