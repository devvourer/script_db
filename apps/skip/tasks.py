from core.celery import app

from .models import YandexFile, Tele2File, PochtaFile
from .services.yandex import YandexService, YandexServiceNoAddress
from .services.tele2 import Tele2Service


@app.task()
def get_content_from_yandex_task(pk: int):
    file = YandexFile.objects.get(pk=pk)
    if file.file_type == YandexFile.FileType.with_address:
        YandexService().get_content(file)
    else:
        YandexServiceNoAddress().get_content(file)


@app.task()
def get_content_from_tele2_task(pk: int):
    file = Tele2File.objects.get(pk=pk)
    Tele2Service().get_content(file)


@app.task()
def get_content_from_pochta_task(pk: int):
    file = Tele2File.objects.get(pk=pk)
    Tele2Service().get_content(file)
