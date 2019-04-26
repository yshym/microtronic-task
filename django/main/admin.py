from django.contrib.gis import admin

from .models import Area


class AreaAdmin(admin.OSMGeoAdmin):
    readonly_fields = (
        'name',
    )
    search_fields = ('name',)

admin.site.register(Area, AreaAdmin)
