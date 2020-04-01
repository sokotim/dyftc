import pytest
from django.http import Http404
from django.test import RequestFactory

from dyftc.cats.models import Cat
from dyftc.cats.views import cat_feeding_view
from dyftc.users.models import User

pytestmark = pytest.mark.django_db


def test_cat_feeding_view(user: User, rf: RequestFactory, cat: Cat):
    request = rf.get("/fake-url/")
    request.user = user

    with pytest.raises(Http404):
        assert cat_feeding_view(request, cat.slug)

    cat.feeders.add(user)
    cat.save()

    response = cat_feeding_view(request, cat.slug)

    assert response.status_code == 302
    assert response.url == cat.get_absolute_url()
