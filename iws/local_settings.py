# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2018 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

import os
from geonode.settings import *

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

MEDIA_ROOT = os.getenv('MEDIA_ROOT', os.path.join(PROJECT_ROOT, "uploaded"))

STATIC_ROOT = os.getenv('STATIC_ROOT',
                        os.path.join(PROJECT_ROOT, "static_root")
                        )

#disable language support
USE_I18N = 'False'
USE_L10N = 'False'
LANGUAGES = (
    ('en', 'English'),
)
 
# Make this unique, and don't share it with anybody.
SECRET_KEY = os.getenv('SECRET_KEY', "{{ secret_key }}")
  
# per-deployment settings should go here
SITE_HOST_NAME = os.getenv('SITE_HOST_NAME', "localhost")
SITE_HOST_PORT = os.getenv('SITE_HOST_PORT', "8000")
SITEURL = os.getenv('SITEURL', "https://%s:%s/" % (SITE_HOST_NAME, SITE_HOST_PORT))


# SECRET_KEY = '************************'
#SITEURL = "https://150.178.42.78"
SITEURL = os.getenv('SITE_URL', "https://iws.seastorms.eu")

ALLOWED_HOSTS = [os.getenv('SITE_HOST'), 'localhost', 'iws.ismar.cnr.it', 'django:8000', 'django', 'iws.seastorms.eu', 'www.seastorms.eu', 'cyber.goats.se', 'seastorms.eu']

PROXY_ALLOWED_HOSTS = ('ows.emodnet-bathymetry.eu', 'emodnet-physics.eu', 'data.adriplan.eu', 'atlas.shape-ipaproject.eu', 'www.seastorms.eu', 'iws.ismar.cnr.it')
DEFAULT_LAYER_FORMAT = "image/png"

TIME_ZONE = 'Europe/Rome'

DEBUG=True

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.getenv('GEONODE_DATABASE_NAME', 'geonode'),
        'USER': os.getenv('GEONODE_DATABASE_NAME', 'geonode'),
        'PASSWORD': os.getenv('GEONODE_DATABASE_PASSWORD', 'geonode'),
        'HOST': os.getenv('GEONODE_DATABASE_HOST', 'localhost'),
        'PORT': os.getenv('GEONODE_PORT', '5432'),
        # 'NAME': 'geonode',
        # 'USER': 'geonode',
        # 'PASSWORD': 'geonode',
        # 'HOST': 'localhost',
        # 'PORT': '5432',
        'CONN_TOUT': 900,
    },
    # vector datastore for uploads
    'datastore': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        # 'ENGINE': '', # Empty ENGINE name disables
        'NAME': os.getenv('GEONODE_GEODATABASE', 'geonode_data'),
        'USER': os.getenv('GEONODE_GEODATABASE', 'geonode'),
        'PASSWORD': os.getenv('GEONODE_GEODATABASE_PASSWORD', 'geonode'),
        'HOST': os.getenv('GEONODE_DATABASE_HOST', 'localhost'),
        'PORT': os.getenv('GEONODE_PORT', '5432'),
        # 'NAME': 'geonode_data',
        # 'USER': 'geonode',
        # 'PASSWORD': 'geonode',
        # 'HOST': 'localhost',
        # 'PORT': '5432',
        'CONN_TOUT': 900,
    },

    # temporarydb
    'seastorm': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        # 'ENGINE': '', # Empty ENGINE name disables
        'NAME': os.getenv('SEASTORM_NAME', 'seastorm'),
        'USER': os.getenv('SEASTORM_NAME', 'geonode'),
        'PASSWORD': os.getenv('SEASTORM_PASSWORD', 'geonode'),
        'HOST': os.getenv('GEONODE_DATABASE_HOST', 'localhost'),
        'PORT': os.getenv('GEONODE_PORT', '5432'),
        'CONN_TOUT': 900,
    },
    'dss_pharos_db': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':  os.getenv('DSS_PHAROS_NAME', 'dss_pharos'),
        'USER': os.getenv('DSS_PHAROS_NAME', 'geonode'),
        'PASSWORD': os.getenv('DSS_PHAROS_PASSWORD', 'geonode'),
        'HOST': os.getenv('GEONODE_DATABASE_HOST', 'localhost'),
        'PORT': os.getenv('GEONODE_PORT', '5432'),
    },

    'measurements': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.getenv('MEASUREMENTS_GEODATABASE', 'measurements'),
        'USER': os.getenv('MEASUREMENTS_GEODATABASE', 'geonode'),
        'PASSWORD': os.getenv('MEASUREMENTS_GEODATABASE_PASSWORD', 'geonode'),
        'HOST': os.getenv('MEASUREMENTS_DATABASE_HOST', 'localhost'),
        'PORT': os.getenv('MEASUREMENTS_PORT', '5432'),
    }

}

GEOSERVER_LOCATION = os.getenv(
    'GEOSERVER_LOCATION', 'http://localhost:8080/geoserver/'
)

GEOSERVER_PUBLIC_LOCATION = os.getenv(
    'GEOSERVER_PUBLIC_LOCATION', '{}/geoserver/'.format(SITEURL)
    #'GEOSERVER_PUBLIC_LOCATION', 'https://iws.ismar.cnr.it/geoserver/'
)

OGC_SERVER_DEFAULT_USER = os.getenv(
    'GEOSERVER_ADMIN_USER', 'admin'
)

OGC_SERVER_DEFAULT_PASSWORD = os.getenv(
    'GEOSERVER_ADMIN_PASSWORD', 'Ora7@cr3AT1vo5%PR0cavi4!'
)

# OGC (WMS/WFS/WCS) Server Settings
OGC_SERVER = {
    'default': {
        'BACKEND': 'geonode.geoserver',
        'LOCATION': GEOSERVER_LOCATION,
        'LOGIN_ENDPOINT': 'j_spring_oauth2_geonode_login',
        'LOGOUT_ENDPOINT': 'j_spring_oauth2_geonode_logout',
        # PUBLIC_LOCATION needs to be kept like this because in dev mode
        # the proxy won't work and the integration tests will fail
        # the entire block has to be overridden in the local_settings
        'PUBLIC_LOCATION': GEOSERVER_PUBLIC_LOCATION,
        'USER': OGC_SERVER_DEFAULT_USER,
        'WEB_UI_LOCATION': GEOSERVER_PUBLIC_LOCATION,
        'PASSWORD': OGC_SERVER_DEFAULT_PASSWORD,
        'MAPFISH_PRINT_ENABLED': True,
        'PRINT_NG_ENABLED': True,
        'GEONODE_SECURITY_ENABLED': True,
        'GEOFENCE_SECURITY_ENABLED': True,
        'GEOGIG_ENABLED': False,
        'WMST_ENABLED': False,
        'BACKEND_WRITE_ENABLED': True,
        'WPS_ENABLED': False,
        'LOG_FILE': '%s/geoserver/data/logs/geoserver.log' % os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir)),
        # Set to dictionary identifier of database containing spatial data in DATABASES dictionary to enable
        'DATASTORE': 'datastore',
        'PG_GEOGIG': False,
        'TIMEOUT': 10  # number of seconds to allow for HTTP requests
    }
}

# WARNING: Map Editing is affected by this. GeoExt Configuration is cached for 5 minutes
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': '/var/tmp/django_cache',
#     }
# }

# If you want to enable Mosaics use the following configuration
UPLOADER = {
    # 'BACKEND': 'geonode.rest',
    'BACKEND': 'geonode.importer',
    'OPTIONS': {
        'TIME_ENABLED': True,
        'MOSAIC_ENABLED': False,
        'GEOGIG_ENABLED': False,
    },
    'SUPPORTED_CRS': [
        'EPSG:4326',
        'EPSG:3785',
        'EPSG:3857',
        'EPSG:900913',
        'EPSG:32647',
        'EPSG:32736'
    ],
    'SUPPORTED_EXT': [
        '.shp',
        '.csv',
        '.kml',
        '.kmz',
        '.json',
        '.geojson',
        '.tif',
        '.tiff',
        '.geotiff',
        '.gml',
        '.xml'
    ]
}

CATALOGUE = {
    'default': {
        # The underlying CSW implementation
        # default is pycsw in local mode (tied directly to GeoNode Django DB)
        'ENGINE': 'geonode.catalogue.backends.pycsw_local',
        # pycsw in non-local mode
        # 'ENGINE': 'geonode.catalogue.backends.pycsw_http',
        # GeoNetwork opensource
        # 'ENGINE': 'geonode.catalogue.backends.geonetwork',
        # deegree and others
        # 'ENGINE': 'geonode.catalogue.backends.generic',

        # The FULLY QUALIFIED base url to the CSW instance for this GeoNode
        'URL': '%s/catalogue/csw' % SITEURL,
        # 'URL': 'http://localhost:8080/geonetwork/srv/en/csw',
        # 'URL': 'http://localhost:8080/deegree-csw-demo-3.0.4/services',

        # login credentials (for GeoNetwork)
        'USER': 'admin',
        'PASSWORD': 'admin',
        'ALTERNATES_ONLY': True,
    }
}

# pycsw settings
PYCSW = {
    # pycsw configuration
    'CONFIGURATION': {
        # uncomment / adjust to override server config system defaults
        # 'server': {
        #    'maxrecords': '10',
        #    'pretty_print': 'true',
        #    'federatedcatalogues': 'http://catalog.data.gov/csw'
        # },
        'metadata:main': {
            'identification_title': 'GeoNode Catalogue',
            'identification_abstract': 'GeoNode is an open source platform' \
            ' that facilitates the creation, sharing, and collaborative use' \
            ' of geospatial data',
            'identification_keywords': 'sdi, catalogue, discovery, metadata,' \
            ' GeoNode',
            'identification_keywords_type': 'theme',
            'identification_fees': 'None',
            'identification_accessconstraints': 'None',
            'provider_name': 'Organization Name',
            'provider_url': SITEURL,
            'contact_name': 'Lastname, Firstname',
            'contact_position': 'Position Title',
            'contact_address': 'Mailing Address',
            'contact_city': 'City',
            'contact_stateorprovince': 'Administrative Area',
            'contact_postalcode': 'Zip or Postal Code',
            'contact_country': 'Country',
            'contact_phone': '+xx-xxx-xxx-xxxx',
            'contact_fax': '+xx-xxx-xxx-xxxx',
            'contact_email': 'Email Address',
            'contact_url': 'Contact URL',
            'contact_hours': 'Hours of Service',
            'contact_instructions': 'During hours of service. Off on ' \
            'weekends.',
            'contact_role': 'pointOfContact',
        },
        'metadata:inspire': {
            'enabled': 'true',
            'languages_supported': 'eng,gre',
            'default_language': 'eng',
            'date': 'YYYY-MM-DD',
            'gemet_keywords': 'Utility and governmental services',
            'conformity_service': 'notEvaluated',
            'contact_name': 'Organization Name',
            'contact_email': 'Email Address',
            'temp_extent': 'YYYY-MM-DD/YYYY-MM-DD',
        }
    }
}

# GeoNode javascript client configuration

# default map projection
# Note: If set to EPSG:4326, then only EPSG:4326 basemaps will work.
DEFAULT_MAP_CRS = "EPSG:3857"

# Where should newly created maps be focused?
DEFAULT_MAP_CENTER = (0, 0)

# How tightly zoomed should newly created maps be?
# 0 = entire world;
# maximum zoom is between 12 and 15 (for Google Maps, coverage varies by area)
DEFAULT_MAP_ZOOM = 0

# Default preview library
# GEONODE_CLIENT_LAYER_PREVIEW_LIBRARY = 'geoext'  # DEPRECATED use HOOKSET instead
GEONODE_CLIENT_HOOKSET = "geonode.client.hooksets.GeoExtHookSet"

# To enable the REACT based Client enable those
# INSTALLED_APPS += ('geonode-client', )
# GEONODE_CLIENT_LAYER_PREVIEW_LIBRARY = 'react'  # DEPRECATED use HOOKSET instead
# GEONODE_CLIENT_HOOKSET = "geonode.client.hooksets.ReactHookSet"

# To enable the Leaflet based Client enable those
# GEONODE_CLIENT_LAYER_PREVIEW_LIBRARY = 'leaflet'  # DEPRECATED use HOOKSET instead
# GEONODE_CLIENT_HOOKSET = "geonode.client.hooksets.LeafletHookSet"

# To enable the MapStore2 based Client enable those
# INSTALLED_APPS += ('geonode_mapstore_client', )
# GEONODE_CLIENT_LAYER_PREVIEW_LIBRARY = 'mapstore'  # DEPRECATED use HOOKSET instead
# GEONODE_CLIENT_HOOKSET = "geonode_mapstore_client.hooksets.MapStoreHookSet"

# LEAFLET_CONFIG = {
#    'TILES': [
#        # Find tiles at:
#        # http://leaflet-extras.github.io/leaflet-providers/preview/
#
#        # Map Quest
#        ('Map Quest',
#         'http://otile4.mqcdn.com/tiles/1.0.0/osm/{z}/{x}/{y}.png',
#         'Tiles Courtesy of <a href="http://www.mapquest.com/">MapQuest</a> '
#         '&mdash; Map data &copy; '
#         '<a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'),
#        # Stamen toner lite.
#        # ('Watercolor',
#        #  'http://{s}.tile.stamen.com/watercolor/{z}/{x}/{y}.png',
#        #  'Map tiles by <a href="http://stamen.com">Stamen Design</a>, \
#        #  <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; \
#        #  <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, \
#        #  <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>'),
#        # ('Toner Lite',
#        #  'http://{s}.tile.stamen.com/toner-lite/{z}/{x}/{y}.png',
#        #  'Map tiles by <a href="http://stamen.com">Stamen Design</a>, \
#        #  <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; \
#        #  <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, \
#        #  <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>'),
#    ],
#    'PLUGINS': {
#        'esri-leaflet': {
#            'js': 'lib/js/esri-leaflet.js',
#            'auto-include': True,
#        },
#        'leaflet-fullscreen': {
#            'css': 'lib/css/leaflet.fullscreen.css',
#            'js': 'lib/js/Leaflet.fullscreen.min.js',
#            'auto-include': True,
#        },
#    },
#    'SRID': 3857,
#    'RESET_VIEW': False
#}

ALT_OSM_BASEMAPS = os.environ.get('ALT_OSM_BASEMAPS', False)
CARTOGEONODE_BASEMAPS = os.environ.get('CARTOGEONODE_BASEMAPS', False)
STAMEN_BASEMAPS = os.environ.get('STAMEN_BASEMAPS', False)
THUNDERFOREST_BASEMAPS = os.environ.get('THUNDERFOREST_BASEMAPS', False)
MAPBOX_ACCESS_TOKEN = os.environ.get('MAPBOX_ACCESS_TOKEN', None)
BING_API_KEY = os.environ.get('BING_API_KEY', None)
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY', None)

MAP_BASELAYERS = [{
    "source": {"ptype": "gxp_olsource"},
    "type": "OpenLayers.Layer",
    "args": ["No background"],
    "name": "background",
    "visibility": False,
    "fixed": True,
    "group":"background"
},
    # {
    #     "source": {"ptype": "gxp_olsource"},
    #     "type": "OpenLayers.Layer.XYZ",
    #     "title": "TEST TILE",
    #     "args": ["TEST_TILE", "http://test_tiles/tiles/${z}/${x}/${y}.png"],
    #     "name": "background",
    #     "attribution": "&copy; TEST TILE",
    #     "visibility": False,
    #     "fixed": True,
    #     "group":"background"
    # },
    {
    "source": {"ptype": "gxp_osmsource"},
    "type": "OpenLayers.Layer.OSM",
    "name": "mapnik",
    "visibility": True,
    "fixed": True,
    "group": "background"
},{
    "source": {"ptype": "gxp_olsource"},
    "type": "OpenLayers.Layer.XYZ",
    "title": "Google Map tiles",
    "args": ["Google Map Tiles", "https://mt2.google.com/vt/lyrs=m&x=${x}&y=${y}&z=${z}"],
    "name": "Google Map",
    "attribution": "&copy; Google",
    "visibility": True,
    "wrapDateLine": True,
    "fixed": True,
    "group":"background"
}]

if 'geonode.geoserver' in INSTALLED_APPS:
    LOCAL_GEOSERVER = {
        "source": {
            "ptype": "gxp_wmscsource",
            "url": OGC_SERVER['default']['PUBLIC_LOCATION'] + "wms",
            "restUrl": "/gs/rest"
        }
    }
    baselayers = MAP_BASELAYERS
    MAP_BASELAYERS = [LOCAL_GEOSERVER]
    MAP_BASELAYERS.extend(baselayers)

# Use kombu broker by default
# REDIS_URL = 'redis://localhost:6379/1'
# BROKER_URL = REDIS_URL
# CELERY_RESULT_BACKEND = REDIS_URL
CELERYD_HIJACK_ROOT_LOGGER = True
CELERYD_CONCURENCY = 1
# Set this to False to run real async tasks
CELERY_ALWAYS_EAGER = True
# CELERYD_LOG_FILE = None
CELERYD_LOG_FILE = '/var/log/celery.log'
CELERY_REDIRECT_STDOUTS = True
CELERYD_LOG_LEVEL = 1

# Haystack Search Backend Configuration. To enable,
# first install the following:
# - pip install django-haystack
# - pip install elasticsearch==2.4.0
# - pip install woosh
# - pip install pyelasticsearch
# Set HAYSTACK_SEARCH to True
# Run "python manage.py rebuild_index"
# HAYSTACK_SEARCH = False
# Avoid permissions prefiltering
SKIP_PERMS_FILTER = False
# Update facet counts from Haystack
HAYSTACK_FACET_COUNTS = True
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch2_backend.Elasticsearch2SearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
    #    'db': {
    #        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    #        'EXCLUDED_INDEXES': ['thirdpartyapp.search_indexes.BarIndex'],
    #        }
}
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
# HAYSTACK_SEARCH_RESULTS_PER_PAGE = 20

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d '
                      '%(thread)d %(message)s'
        },
        'simple': {
            'format': '%(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR', 'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    "loggers": {
        "django": {
            "handlers": ["console"], "level": "ERROR", },
        "geonode": {
            "handlers": ["console"], "level": "DEBUG", },
        "gsconfig.catalog": {
            "handlers": ["console"], "level": "DEBUG", },
        "owslib": {
            "handlers": ["console"], "level": "DEBUG", },
        "pycsw": {
            "handlers": ["console"], "level": "ERROR", },
    },
}

# Additional settings
CORS_ORIGIN_ALLOW_ALL = True

GEOIP_PATH = "/usr/local/share/GeoIP"

# add following lines to your local settings to enable monitoring
MONITORING_ENABLED = True

if MONITORING_ENABLED:
    if 'geonode.contrib.monitoring' not in INSTALLED_APPS:
        INSTALLED_APPS += ('geonode.contrib.monitoring',)
    if 'geonode.contrib.monitoring.middleware.MonitoringMiddleware' not in MIDDLEWARE_CLASSES:
        MIDDLEWARE_CLASSES += \
            ('geonode.contrib.monitoring.middleware.MonitoringMiddleware',)
    MONITORING_CONFIG = None
    MONITORING_SERVICE_NAME = 'local-geonode'

#Define email service on GeoNode
EMAIL_ENABLE = True

if EMAIL_ENABLE:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = os.getenv('EMAIL_HOST', 'host.sbagliato')
    #EMAIL_HOST = 'email.ismar.cnr.it'
    DEFAULT_FROM_EMAIL = 'admin-noreply@iws.ismar.cnr.it'
    #SERVER_EMAIL = DEFAULT_FROM_EMAIL
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'iws.seastorms.eu@gmail.com'
    EMAIL_HOST_PASSWORD = 'NETcdf14models'
    EMAIL_USE_TLS = True
    #DEFAULT_FROM_EMAIL = 'Example.com <no-reply@localhost>'
# smtp.gmail.com iws.seastorms.eu@gmail.com NETcdf14models 587
# REGISTRATION

THEME_ACCOUNT_CONTACT_EMAIL = 'iws.seastorms.eu@gmail.com'

ACCOUNT_OPEN_SIGNUP = False
ACCOUNT_EMAIL_CONFIRMATION_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True
ACCOUNT_APPROVAL_REQUIRED = True



# Documents Thumbnails
UNOCONV_ENABLE = True

if UNOCONV_ENABLE:
    UNOCONV_EXECUTABLE = os.getenv('UNOCONV_EXECUTABLE', '/usr/bin/unoconv')
    UNOCONV_TIMEOUT = os.getenv('UNOCONV_TIMEOUT', 30)  # seconds

# Advanced Security Workflow Settings
CLIENT_RESULTS_LIMIT = 20
API_LIMIT_PER_PAGE = 1000
FREETEXT_KEYWORDS_READONLY = False
RESOURCE_PUBLISHING = False
ADMIN_MODERATE_UPLOADS = False
GROUP_PRIVATE_RESOURCES = False
GROUP_MANDATORY_RESOURCES = False
MODIFY_TOPICCATEGORY = True
USER_MESSAGES_ALLOW_MULTIPLE_RECIPIENTS = True
DISPLAY_WMS_LINKS = True

# For more information on available settings please consult the Django docs at
# https://docs.djangoproject.com/en/dev/ref/settings

#dss_pharos temporary settings
INSTALLED_APPS += (
                   # 'dss_pharos',
                   'ckeditor',
                   'ckeditor_uploader',
                   'django_bootstrap_breadcrumbs',
                   )
CKEDITOR_UPLOAD_PATH = 'cked_upload'

#set the mapa number for sea storm atlas, used in redirect into urls.py 
STORM_ATLAS_MAP = 165

LOGOUT_REDIRECT_URL = '/'
