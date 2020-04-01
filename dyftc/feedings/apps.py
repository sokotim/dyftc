from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FeedingsConfig(AppConfig):
    name = "dyftc.feedings"
    verbose_name = _("feedings")
