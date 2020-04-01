from factory import DjangoModelFactory, SubFactory, post_generation

from dyftc.feedings.models import Feeding
from dyftc.users.tests.factories import UserFactory


class FeedingFactory(DjangoModelFactory):
    feeder = SubFactory(UserFactory)

    class Meta:
        model = Feeding

    @post_generation
    def cats(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for cat in extracted:
                self.cats.add(cat)
