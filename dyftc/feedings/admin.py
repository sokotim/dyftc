from django.contrib import admin

from dyftc.feedings.models import Feeding


@admin.register(Feeding)
class FeedingAdmin(admin.ModelAdmin):
    autocomplete_fields = ("feeder", "cats")
    date_hierarchy = "created"
    search_fields = ("cats__name",)
