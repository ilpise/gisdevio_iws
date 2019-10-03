from django.db import models
from django.contrib.gis.db import models as gismodel
from geonode import settings
from django.contrib.gis.geos import Point

class Setting(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    sl_reference = models.FloatField(blank=True, null=True)
    sl_notification_threshold = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return str(self.user.email)

