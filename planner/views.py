from django.shortcuts import render
from .models import Lesson, Subject, Grade

def index(request):
    # Отримуємо всі предмети
    subjects = Subject.objects.all()

    # Для кожного предмету отримуємо пов'язані класи
    subjects_with_grades = []
    for subject in subjects:
        grades = Grade.objects.filter(lesson__subject=subject).distinct()
        if grades:  # Перевіряємо, чи є пов'язані класи
            subjects_with_grades.append({'subject': subject, 'grades': grades})

    context = {
        'subjects_with_grades': subjects_with_grades,
    }
    return render(request, 'planner/index.html', context)

def lesson_list(request, subject_id, grade_id):
    lessons = Lesson.objects.filter(subject_id=subject_id, grade_id=grade_id).order_by('date', 'time')
    return render(request, 'planner/lesson_list.html', {'lessons': lessons})