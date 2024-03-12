import logging

from collections import OrderedDict
from django.utils.translation import ugettext as _

from .. import enumerations
from geonode.services.utils import parse_services_types
from geonode.services.serviceprocessors import get_available_service_types

logger = logging.getLogger(__name__)


def get_available_service_types_polls():
    # LGTM: Fixes - Module uses member of cyclically imported module, which can lead to failure at import time.
    from geonode.services.serviceprocessors.wms import GeoNodeServiceHandler, WmsServiceHandler
    from geonode.services.serviceprocessors.arcgis import ArcImageServiceHandler, ArcMapServiceHandler
    from .thredds import GeoNodeServiceHandler, ThreddsWmsServiceHandler

    default = OrderedDict({
        enumerations.THREDDS: {"OWS": True, "handler": ThreddsWmsServiceHandler, "label": _('THREDDS Service')},
    })

    return OrderedDict({**default, **parse_services_types()})

def get_service_handler_thredds(base_url, service_type=enumerations.AUTO, service_id=None):
    """Return the appropriate remote service handler for the input URL.
    If the service type is not explicitly passed in it will be guessed from
    """
    handlers = get_available_service_types()
    handlers_thredds = get_available_service_types_polls()
    handlers.update(handlers_thredds)

    handler = handlers.get(service_type, {}).get("handler")

    print('handler __init__.py')
    print(handler)

    try:
        service = handler(base_url, service_id)
    except Exception:
        logger.exception(
            msg=f"Could not parse service {base_url}")
        raise
    return service