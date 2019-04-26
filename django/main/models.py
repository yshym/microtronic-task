from django.contrib.gis.db import models


class Area(models.Model):
    name = models.CharField(max_length=150)
    polygon = models.PolygonField()

    def __str__(self):
        return self.name
