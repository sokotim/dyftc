from factory import DjangoModelFactory, Faker

from dyftc.cats.models import Cat


class CatFactory(DjangoModelFactory):
    name = Faker("first_name")

    class Meta:
        model = Cat
        django_get_or_create = ["name"]
