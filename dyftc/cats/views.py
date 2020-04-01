from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from dyftc.cats.models import Cat


class CatDetailView(LoginRequiredMixin, DetailView):
    model = Cat

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["feeders"] = self.object.feeders.all()
        return context


cat_detail_view = CatDetailView.as_view()
