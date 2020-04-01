from django.urls import path

from dyftc.feedings.views import feeding_detail_view

app_name = "feedings"

urlpatterns = [path("<int:pk>/", feeding_detail_view, name="detail")]
