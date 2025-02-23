from django.contrib import admin
from .models import Subject, Grade, Material, Lesson
# Register your models here.

admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(Material)
admin.site.register(Lesson)