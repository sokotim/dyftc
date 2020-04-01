import pytest
from django.urls import resolve, reverse

from dyftc.cats.models import Cat

pytestmark = pytest.mark.django_db


def test_detail(cat: Cat):
    assert reverse("cats:detail", kwargs={"slug": cat.slug}) == f"/cats/{cat.slug}/"
    assert resolve(f"/cats/{cat.slug}/").view_name == "cats:detail"
