from django.urls import include, re_path
from django.conf.urls import url

from . import views

urlpatterns = (
    re_path('test/', views.index, name="pisdev"),
)

