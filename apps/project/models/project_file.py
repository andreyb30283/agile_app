#  В приложении project создайте новую модель ProjectFile:
# file_name (Строковое поле, максимальная длина - 120 символов)
# file_path (Поле загрузки файлов, таргет сохранения - папка documents)
# created_at (Дата создания файла, автозаполняется при создании нового файла)
# Отображение объектов по полу name (магический метод __str__)
# Сортировка записей по дате создания в порядке убывания
# В модели Project создайте новое поле files, которое будет связывать проекты и файлы связью Многие ко Многим, связующее поле - project.
# В модели Project добавьте динамическое поле count_of_files через декоратор @property, которое будет высчитывать количество файлов для проекта.
# Проведите миграции, убедиться, что всё работает, запустив сервер.
from django.db import models


class ProjectFile(models.Model):
    file_name = models.CharField(max_length=120)
    file_path = models.FileField(upload_to="documents/")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.file_name

    class Meta:
        ordering = ["created_at"]