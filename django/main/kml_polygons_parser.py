from lxml import etree
import re
from .models import Area
from django.contrib.gis.geos import Polygon

def split(size, arr):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr = arr[size:]
     arrs.append(arr)
     return arrs


class PolygonsParser:
    def __init__(self, path_to_file):
        self._path_to_file = path_to_file

    @property
    def path_to_file(self):
        return self._path_to_file

    def get_areas(self):
        tree = etree.parse(self._path_to_file)

        document = tree.find('Document')
        placemarks = document.findall('Placemark')

        areas = []

        for placemark in placemarks:
            name = placemark.find('name').text

            if placemark.find('Polygon') is not None:
                coords = re.split(',| ', placemark.find('Polygon').find('outerBoundaryIs').find('LinearRing').find('coordinates').text)
                coords = list(map(float, coords))
                coords = list(filter(lambda x: x != 0, coords))
                coords = split(2, coords)
                areas.append((name, coords))

        return areas

    def create_polygons(self):
        areas = self.get_areas()
        for name, coords in areas:
            coords.append(coords[0])
            Area.objects.create(
                name=name,
                polygon=Polygon(coords)
            )
