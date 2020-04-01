import pytest

from dyftc.feedings.models import Feeding

pytestmark = pytest.mark.django_db


def test_feeding_get_absolute_url(feeding: Feeding):
    assert feeding.get_absolute_url() == f"/feedings/{feeding.pk}/"
