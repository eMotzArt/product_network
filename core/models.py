from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.db import models

from core.manager import CustomUserManager


class Country(models.Model):
    country_name = models.CharField(max_length=50)

    def __str__(self):
        return self.country_name


class City(models.Model):
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name


class Contact(models.Model):
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    street = models.CharField(max_length=50, blank=False)
    house = models.IntegerField(blank=False)


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()


    class Role(models.IntegerChoices):
        factory = 0, "Завод-производитель"
        retailer = 1, "Ретейлер"
        trader = 2, "Индивидуальный предприниматель"


    name = models.CharField(max_length=150, blank=False, unique=True, verbose_name='Название')
    email = models.EmailField(blank=False, unique=True, verbose_name='Адрес email')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name='Контакты')
    # products = models.ForeignKey(Product, blank=True, related_name="owner", verbose_name='Товары')
    supplier = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, verbose_name='Поставщик')
    debts = models.FloatField(default=0.00, verbose_name='Долг')
    role = models.PositiveSmallIntegerField(choices=Role.choices, verbose_name="Роль предприятия\ИП")
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    def __str__(self):
        return self.email
