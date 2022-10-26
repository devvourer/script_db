from django.apps import AppConfig
from django.core.signals import request_finished


class SkipConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.skip'

    def ready(self):
        from . import signals
