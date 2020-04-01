import pytest
from django.urls import resolve, reverse

from dyftc.feedings.models import Feeding

pytestmark = pytest.mark.django_db


def test_detail(feeding: Feeding):
    assert (
        reverse("feedings:detail", kwargs={"pk": feeding.pk})
        == f"/feedings/{feeding.pk}/"
    )
    assert resolve(f"/feedings/{feeding.pk}/").view_name == "feedings:detail"
