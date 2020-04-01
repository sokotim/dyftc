from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Cat(models.Model):
    name = models.CharField(_("name"), max_length=50)
    slug = AutoSlugField(populate_from="name", unique=True)
    feeders = models.ManyToManyField(
        User, verbose_name=_("feeders"), related_name="cats"
    )

    class Meta:
        verbose_name = _("cat")
        verbose_name_plural = _("cats")
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cats:detail", kwargs={"slug": self.slug})
