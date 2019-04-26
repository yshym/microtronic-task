from django.core.management.base import BaseCommand, CommandError
from main.kml_polygons_parser import PolygonsParser
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Loads all the areas'

    def add_arguments(self, parser):
        parser.add_argument('--path')

    def handle(self, *args, **options):
        try:
            if options.get('path'):
                polygons_parser = PolygonsParser(options.get('path'))
            else:
                polygons_parser = PolygonsParser(
                    os.path.join(
                        settings.BASE_DIR,
                        'main/data/microtronic_polygons.kml'
                    )
                )
            polygons_parser.create_polygons()
        except:
            raise CommandError('You used uncorrect path!')

        self.stdout.write(self.style.SUCCESS('Areas were loaded successfully!'))
