# Generated by Django 4.1.2 on 2022-10-26 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skip', '0002_alter_yandex_address_house_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tele2file',
            name='file',
            field=models.FileField(upload_to='tele2_files'),
        ),
    ]
