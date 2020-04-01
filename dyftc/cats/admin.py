from django.contrib import admin

from dyftc.cats.models import Cat


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    autocomplete_fields = ("feeders",)
    search_fields = ("name",)
