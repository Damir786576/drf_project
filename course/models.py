from django.db import models


class Course(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Укажите название курса",
    )
    preview = models.ImageField(
        upload_to="courses/previews",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите изображение курса",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
        help_text="Введите описание курса",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
