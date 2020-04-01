from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CatsConfig(AppConfig):
    name = "dyftc.cats"
    verbose_name = _("cats")
