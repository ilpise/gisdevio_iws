# from django.contrib import admin
from django.contrib.gis import admin


from .models import CoastalSegment, StormEvent, Sea

class CoastalSegmentAdmin(admin.ModelAdmin):
    list_display = ('code', 'partition','subregion')
    
    
class StormEventAdmin(admin.OSMGeoAdmin):
    list_display = ('id', 'date_start','area_code', 'area_partition')
    list_filter = ['area_code', 'area_partition', 'date_start']
    openlayers_url = '//openlayers.org/api/2.13/OpenLayers.js'
    default_lat = 42.115373
    default_lon = 15.940648

    fieldsets = ((None, {
        'fields': ('coastalsegment',
                   'geom',
                   ('date_start', 'date_end',),
                   'is_aggregated',
                   'flooding_level',
                   'origin',
                   'comments'
                   )
    },),
                 ('Events details', {
                     'classes': ('collapse',),
                     'fields': ('evts_total',
                                ('evts_coast_erosion', 'evts_flooding', 'evts_defence_damage'),
                                ('evts_infrastructure_damage', 'evts_businesses_damage',),
                                 'evts_documents'
                    )
                 }),
    )
    filter_horizontal = ('evts_documents',)
    pass


class SeaAdmin(admin.ModelAdmin):
    pass


admin.site.register(CoastalSegment, CoastalSegmentAdmin)
admin.site.register(StormEvent, StormEventAdmin)

