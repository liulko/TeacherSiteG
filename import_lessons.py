import csv
from datetime import datetime
from planner.models import Lesson, Subject, Grade
from django.db import transaction

def import_lessons_from_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        with transaction.atomic():  # Для забезпечення цілісності даних
            for row in reader:
                try:
                    subject = Subject.objects.get(name=row['subject'])
                    grade = Grade.objects.get(number=row['grade'])
                except Subject.DoesNotExist:
                    print(f"Предмет '{row['subject']}' не знайдено!")
                    continue
                except Grade.DoesNotExist:
                    print(f"Клас '{row['grade']}' не знайдено!")
                    continue

                    # Конвертуємо дату з DD.MM.YYYY в YYYY-MM-DD
                try:
                    # ... (код для отримання subject та grade)

                    # Конвертуємо дату
                    date_str = row['date']
                    date_object = datetime.strptime(date_str, '%d.%m.%Y').date()

                    Lesson.objects.create(
                        subject=subject,
                        grade=grade,
                        date=date_object,
                        title=row['lesson_content'],
                        notes=row['notes'],
                        lesson_number=row['lesson_number']  # Передаємо номер уроку з файлу
                    )
                except Exception as e:
                    print(f"Помилка імпорту рядка: {row}. Помилка: {e}")
                    continue
    print("Імпорт завершено!")

# Запуск імпорту (приклад)
if __name__ == '__main__':
    file_path = 'plans_as_csv/5m.csv'  # Замініть на шлях до вашого файлу
    import_lessons_from_csv(file_path)