from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import YandexFile, Tele2File, PochtaFile
from .tasks import get_content_from_yandex_task, get_content_from_tele2_task


@receiver(post_save, sender=YandexFile)
def get_content_from_yandex(sender, instance, created, **kwargs):
    if created:
        get_content_from_yandex_task.apply_async((instance.pk,), countdown=5)


@receiver(post_save, sender=Tele2File)
def get_content_from_tele2(sender, instance, created, **kwargs):
    if created:
        get_content_from_tele2_task.apply_async((instance.pk,), countdown=5)


# @receiver(post_save, sender=PochtaFile)
# def get_content_from_pochta(sender, instance, created, **kwargs):
#     if created:
#         get_content_from_pochta_task.apply_async((instance.pk,), countdown=5)
