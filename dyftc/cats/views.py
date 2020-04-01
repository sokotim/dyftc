from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView

from dyftc.cats.models import Cat
from dyftc.feedings.models import Feeding


class CatDetailView(LoginRequiredMixin, DetailView):
    model = Cat

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["feeders"] = self.object.feeders.all()
        context["last_feeding"] = self.object.feedings.first()
        return context


cat_detail_view = CatDetailView.as_view()


@login_required
def cat_feeding_view(request, slug):
    cat = get_object_or_404(Cat, slug=slug, feeders=request.user)
    feeding = Feeding(feeder=request.user)
    feeding.save()
    feeding.cats.add(cat)
    return HttpResponseRedirect(reverse("cats:detail", args=(cat.slug,)))
