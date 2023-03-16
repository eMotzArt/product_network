from django.contrib.auth import get_user_model
from django.db import models

USER_MODEL = get_user_model()

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    model = models.CharField(max_length=100, verbose_name='Модель')
    count = models.PositiveIntegerField(default=1, verbose_name='Количество')
    release_date = models.DateField(auto_now_add=True, verbose_name='Дата выпуска')
    owner = models.ForeignKey(USER_MODEL, null=True, on_delete=models.CASCADE, verbose_name='Владелец')
    price = models.FloatField(default=0, verbose_name='Цена')

    def __str__(self):
        return f"{self.name}: {self.model}"
    class Meta:
        unique_together = ['name', 'model', 'owner']
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
