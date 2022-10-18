from django.db import models


class Contact(models.Model):
    phone = models.CharField(verbose_name='Номер телефона', max_length=11, null=True)
    name = models.CharField(verbose_name='Имя', max_length=50, null=True)
    surname = models.CharField(verbose_name='Фамилия', max_length=50, null=True)
    patronymic = models.CharField(verbose_name='Отчество', max_length=50, null=True)


class CsvData(models.Model):
    file = models.FileField()
