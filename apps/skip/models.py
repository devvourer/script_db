from django.db import models


class Tele2(models.Model):
    phone = models.CharField(verbose_name='Номер телефона', max_length=11, null=True)
    name = models.CharField(verbose_name='Имя', max_length=50, null=True)
    surname = models.CharField(verbose_name='Фамилия', max_length=50, null=True)
    patronymic = models.CharField(verbose_name='Отчество', max_length=50, null=True)
    act_date = models.DateField()

    class Meta:
        verbose_name = 'Теле2'
        verbose_name_plural = 'Теле2 данные'

    def __str__(self):
        return f'{self.pk} {self.surname} {self.name}'


class Tele2File(models.Model):
    file = models.FileField(upload_to='tele2_files')
    act_date = models.DateField()

    class Meta:
        verbose_name = 'Файл с данными теле2'
        verbose_name_plural = 'Файлы с данными теле2'

    def __str__(self):
        return f'{self.pk} {self.act_date}'


class Yandex(models.Model):
    y_id = models.IntegerField(verbose_name='Id в яндекс')
    first_name = models.CharField(max_length=100, verbose_name='Имя', null=True)
    surname = models.CharField(max_length=50, verbose_name='Фамилия', null=True)
    patronymic = models.CharField(max_length=50, verbose_name='Отчество', null=True)
    email = models.EmailField(null=True, verbose_name='Почта')
    phone_number = models.CharField(max_length=11, null=True, verbose_name='Номер телефона')
    address_city = models.CharField(max_length=50, null=True, verbose_name='Город')
    address_street = models.CharField(max_length=100, null=True, verbose_name='Улица')
    address_house = models.CharField(max_length=100, null=True, verbose_name='Дом')
    address_office = models.CharField(max_length=100, null=True, verbose_name='Офис')

    act_date = models.DateField(verbose_name='Дата акутальности')

    class Meta:
        verbose_name = 'Яндекс данные'
        verbose_name_plural = 'Яндекс данные'

    def __str__(self):
        return f'{self.pk} {self.surname} {self.first_name}'


class YandexBad(models.Model):
    y_id = models.IntegerField(null=True, verbose_name='Id в яндекс')
    first_name = models.CharField(max_length=100, null=True, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия', null=True)
    patronymic = models.CharField(max_length=50, verbose_name='Отчество', null=True)
    email = models.EmailField(null=True, verbose_name='Почта')
    phone_number = models.CharField(max_length=11, null=True, verbose_name='Номер телефона')
    address_city = models.CharField(max_length=100, null=True, verbose_name='Город')
    address_street = models.CharField(max_length=100, null=True, verbose_name='Улица')
    address_house = models.CharField(max_length=100, null=True, verbose_name='Дом')
    address_office = models.CharField(max_length=100, null=True, verbose_name='Офис')

    act_date = models.DateField(verbose_name='Дата акутальности')

    class Meta:
        verbose_name = 'Яндекс не валидные данные'
        verbose_name_plural = 'Яндекс не валидные данные'

    def __str__(self):
        return f'{self.pk} {self.y_id}'


class YandexFile(models.Model):
    class FileType(models.TextChoices):
        no_address = 'no_address', 'без адресов'
        with_address = 'with_addresses', 'с адресами'

    file = models.FileField(upload_to=f'yandex_files')
    file_type = models.CharField(choices=FileType.choices, max_length=14)
    act_date = models.DateField()

    class Meta:
        verbose_name = 'Файл с данными яндекса'
        verbose_name_plural = 'Файлы с данными яндекса'

    def __str__(self):
        return f'{self.pk} {self.file_type} : {self.act_date}'
