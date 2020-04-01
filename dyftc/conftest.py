import pytest

from dyftc.cats.models import Cat
from dyftc.cats.tests.factories import CatFactory
from dyftc.users.models import User
from dyftc.users.tests.factories import UserFactory


@pytest.fixture
def cat() -> Cat:
    return CatFactory()


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()
