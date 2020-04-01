from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

User = get_user_model()


class Feeding(TimeStampedModel):
    cats = models.ManyToManyField(
        "cats.Cat", verbose_name=_("cats"), related_name="feedings"
    )
    feeder = models.ForeignKey(
        User,
        verbose_name=_("feeder"),
        on_delete=models.SET_NULL,
        related_name="feedings",
        null=True,
    )

    class Meta:
        verbose_name = _("feeding")
        verbose_name_plural = _("feedings")
        ordering = ("-created",)

    def __str__(self):
        return "{:%c} {}".format(self.created, ",".join([str(cat) for cat in self.cats.all()]))

    def get_absolute_url(self):
        return reverse("feedings:detail", kwargs={"pk": self.pk})
