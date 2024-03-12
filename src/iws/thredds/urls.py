from django.conf.urls import url
from django.urls import include, re_path


from . import views
# from geonode.thredds import views as serviews
# from . import forms

urlpatterns = [
    url(r'^register_service_wms/$', views.register_service_wms, name="register_service_wms"),
    url(r'^register_thredds/$', views.register_thredds_service, name="register_thredds_service"),
    url(r'^parse_catalog/$', views.parse_catalog, name='parse_catalog'),
    url(r'^follow_catalog/$', views.follow_catalog, name='follow_catalog'),
    re_path(r'^catalogue/', include('iws.pisdev.urls'))
]