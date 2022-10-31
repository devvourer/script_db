from django.contrib import admin

from .models import Tele2File, Tele2, YandexFile, Yandex, YandexBad, Pochta


admin.site.register(Tele2File)
admin.site.register(Tele2)
admin.site.register(Yandex)
admin.site.register(YandexBad)
admin.site.register(YandexFile)
admin.site.register(Pochta)
