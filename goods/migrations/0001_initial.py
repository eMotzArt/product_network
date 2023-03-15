# Generated by Django 4.1.7 on 2023-03-15 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('count', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('release_date', models.DateField(auto_now_add=True, verbose_name='Дата выпуска')),
                ('price', models.FloatField(default=0, verbose_name='Цена')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'unique_together': {('name', 'model', 'owner')},
            },
        ),
    ]
