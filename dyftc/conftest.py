import pytest

from dyftc.cats.models import Cat
from dyftc.cats.tests.factories import CatFactory
from dyftc.feedings.models import Feeding
from dyftc.feedings.tests.factories import FeedingFactory
from dyftc.users.models import User
from dyftc.users.tests.factories import UserFactory


@pytest.fixture
def cat() -> Cat:
    return CatFactory()


@pytest.fixture
def feeding() -> Feeding:
    return FeedingFactory()


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()
