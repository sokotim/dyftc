import pytest

from dyftc.cats.models import Cat

pytestmark = pytest.mark.django_db


def test_cat_get_absolute_url(cat: Cat):
    assert cat.get_absolute_url() == f"/cats/{cat.slug}/"
