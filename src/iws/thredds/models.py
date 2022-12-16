from django.db import models
from geonode.harvesting.models import HarvestableResource


# Create your models here.


""" extend HarvestableResource to set has_time to layer if the external WMS has a time dimension """
# class HarvestableTimeResource(HarvestableResource):
#     has_time = models.BooleanField(default=False)
