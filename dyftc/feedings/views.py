from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from dyftc.feedings.models import Feeding


class FeedingDetailView(LoginRequiredMixin, DetailView):
    model = Feeding

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cats"] = self.object.cats.all()
        return context


feeding_detail_view = FeedingDetailView.as_view()
