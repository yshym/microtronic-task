from django.views.generic import TemplateView
from django.conf import settings

from .models import Area


class HomeView(TemplateView):
    template_name = 'home.djhtml'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['GOOGLE_MAPS_API_KEY'] = settings.GOOGLE_MAPS_API_KEY
        coords_list = []
        for area in Area.objects.all():
            current_coords = area.polygon.coords
            current_coords = list(current_coords)
            current_coords[0] = list(current_coords[0])

            for index, coord in enumerate(current_coords[0]):
                current_coords[0][index] = list(coord)

            coords_list.append(current_coords)

        context['coords_list'] = coords_list
        return context
