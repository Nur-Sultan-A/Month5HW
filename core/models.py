from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=155, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'


class Models(models.Model):
    title = models.CharField(max_length=155, verbose_name='Название')

    category = models.ForeignKey(
        Category,
        verbose_name='Category',
        on_delete=models.CASCADE,
        related_name='models',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Модел'
        verbose_name_plural = 'Модели'