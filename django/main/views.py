from django.views.generic import TemplateView
from django.conf import settings

from .models import Area


def tuple2list(ctuple):
    return list((tuple2list(elt) if isinstance(elt, tuple) else elt for elt in ctuple))


class HomeView(TemplateView):
    template_name = 'home.djhtml'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['GOOGLE_MAPS_API_KEY'] = settings.GOOGLE_MAPS_API_KEY
        context['coords_list'] = [tuple2list(area.polygon.coords) for area in Area.objects.all()]
        return context
