from django.urls import path
from . import views

urlpatterns = [
    path('lessons/<int:subject_id>/<int:grade_id>/', views.lesson_list, name='lesson_list'),
    path('', views.index, name='index'),
]