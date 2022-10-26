from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import YandexFile, Tele2File
from .services.yandex import Service, ServiceNoAddress


@receiver(post_save, sender=YandexFile)
def get_content_from_file(sender, instance, created, **kwargs):
    if created:
        if instance.file_type == YandexFile.FileType.with_address:
            Service().get_content(instance)
        else:
            ServiceNoAddress().get_content(instance)


@receiver(post_save, sender=Tele2File)
def get_content_from_file(sender, instance, created, **kwargs):
    if created:
        Service().get_content(instance)
