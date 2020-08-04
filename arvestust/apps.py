# arvestust:apps
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ArvestustConfig(AppConfig):
    name = 'arvestust'
    verbose_name = _('Arvestust Files and Record-Keeping')

    def ready(self):
        from .models import signals
        from . import audit
