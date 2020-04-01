from django.urls import path

from dyftc.cats.views import cat_detail_view

app_name = "cats"

urlpatterns = [path("<slug:slug>/", cat_detail_view, name="detail")]
