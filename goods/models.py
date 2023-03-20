from django.contrib.auth import get_user_model
from django.db import models

USER_MODEL = get_user_model()

# Create your models here.

class Contact(models.Model):
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=256)
    street = models.CharField(max_length=256)
    house = models.IntegerField(blank=False)
    email = models.EmailField(blank=False, unique=True, verbose_name='Адрес email')


    def __str__(self):
        return f"{self.country}, {self.city}, {self.street}, {self.house}"

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class Supplier(models.Model):
    class Role(models.IntegerChoices):
        factory = 0, "Завод-производитель"
        retailer = 1, "Ретейлер"
        trader = 2, "Индивидуальный предприниматель"


    name = models.CharField(max_length=150, blank=False, unique=True, verbose_name='Наименование')
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, verbose_name='Контактная информация')
    provider = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Поставщик')
    debts = models.FloatField(default=0.00, verbose_name='Долг')
    role = models.PositiveSmallIntegerField(choices=Role.choices, verbose_name="Роль предприятия\ИП")
    products = models.ManyToManyField('Product', related_name='Товары')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    model = models.CharField(max_length=100, verbose_name='Модель')
    release_date = models.DateField(auto_now_add=True, verbose_name='Дата выпуска')

    def __str__(self):
        return f"{self.name}: {self.model}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
