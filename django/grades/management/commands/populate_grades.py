from django.core.management.base import BaseCommand
from grades.models import Student, Teacher, Subject, Grade
import random

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Создание тестовых студентов
        students = [Student.objects.create(name=f'Student {i}', email=f'student{i}@example.com') for i in range(1, 6)]
        
        # Создание тестовых преподавателей
        teachers = [Teacher.objects.create(name=f'Teacher {i}', email=f'teacher{i}@example.com') for i in range(1, 4)]
        
        # Создание тестовых предметов
        subjects = [Subject.objects.create(name=f'Subject {i}', code=f'SUB{i}') for i in range(1, 6)]
        
        # Создание тестовых оценок
        for student in students:
            for _ in range(3):  # Каждому студенту выставим 3 оценки
                Grade.objects.create(
                    student=student,
                    teacher=random.choice(teachers),
                    subject=random.choice(subjects),
                    score=random.randint(1, 100)
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
