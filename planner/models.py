from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва предмету")

    def __str__(self):
        return self.name

class Grade(models.Model):
    number = models.CharField(max_length=10, verbose_name="Номер класу")

    def __str__(self):
        return self.number

class Material(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва матеріалу")
    file = models.FileField(upload_to='materials/', blank=True, null=True, verbose_name="Файл")

    def __str__(self):
        return self.name

class Lesson(models.Model):
    lesson_number = models.IntegerField(verbose_name="Номер уроку", blank=True, null=True)  # Додаємо поле для номера уроку
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, verbose_name="Клас")
    date = models.DateField(verbose_name="Дата")
    title = models.CharField(max_length=255, verbose_name="Зміст уроку")
    time = models.TimeField(blank=True, null=True, verbose_name="Час")
    description = models.TextField(blank=True, null=True, verbose_name="Опис уроку")
    materials = models.ManyToManyField(Material, blank=True, verbose_name="Матеріали")
    homework = models.TextField(blank=True, null=True, verbose_name="Домашнє завдання")
    notes = models.TextField(blank=True, null=True, verbose_name="Примітки")

    def __str__(self):
        return f"{self.subject} - {self.grade} - {self.title} - {self.date}"