import json

from django.shortcuts import render

# Create your views here.


import logging
from siphon.catalog import TDSCatalog

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.utils.translation import ugettext as _

from geonode.services import enumerations

from . import forms

logger = logging.getLogger(__name__)
master = {}


@login_required
def register_service_wms(request):
    if request.method == "POST":
        print('POST')
        print(request.POST)
        form = forms.CreateServiceForm(request.POST)
        if form.is_valid():
            print('VALID FORM')
            service_handler = form.cleaned_data["service_handler"]
            service = service_handler.create_geonode_service(
                owner=request.user)
            try:
                service.full_clean()
            except Exception as e:
                raise Http404(str(e))
            service.save()
            service.keywords.add(*service_handler.get_keywords())

            if service_handler.indexing_method == enumerations.CASCADED:
                service_handler.create_cascaded_store(service)
            service_handler.geonode_service_id = service.id
            request.session[service_handler.url] = service_handler
            logger.debug("Added handler to the session")
            # messages.add_message(
            #     request,
            #     messages.SUCCESS,
            #     _("Service registered successfully")
            # )
            # result = HttpResponseRedirect(
            #     reverse("harvest_resources",
            #             kwargs={"service_id": service.id})
            # )
            result = JsonResponse(reverse("harvest_resources",
                                          kwargs={"service_id": service.id}),
                                  safe=False, status=200
                                  )

        else:
            print('FORM NOT VALID')
            result = JsonResponse("not vaid", safe=False, status=500)

    return result


@login_required
# Questa funzione viene chiamata per tutti i tipi di servizi selezionati nel selectbox
# NOT USED
def register_thredds_service(request):
    service_register_template = "service_register.html"
    # service_register_template = loader.get_template('service_register.html')
    if request.method == "POST":
        form = forms.CreateServiceForm(request.POST)
        # print('--- FORM ---')
        # print(form)
        # print('-- service_handler --')
        # print(form.cleaned_data["service_handler"])
        if form.is_valid():
            # print('FORM VALID')
            catalog_url = form.cleaned_data["url"]
            # print(catalog_url)
            # service_handler = form.cleaned_data["service_handler"]
            # print('views.py service_handler ' + service_handler)
            # service = service_handler.create_geonode_service(
            #     owner=request.user)
            # url =
            # try:
            #     service.full_clean()
            # except Exception as e:
            #     raise Http404(str(e))
            # print(service)
        #     service.save()
        #     service.keywords.add(*service_handler.get_keywords())
        #
        #     if service_handler.indexing_method == enumerations.CASCADED:
        #         service_handler.create_cascaded_store(service)
        #     service_handler.geonode_service_id = service.id
        #     request.session[service_handler.url] = service_handler
        #     logger.debug("Added handler to the session")
        #     messages.add_message(
        #         request,
        #         messages.SUCCESS,
        #         _("Service registered successfully")
        #     )
        #     result = HttpResponseRedirect(
        #         reverse("harvest_resources",
        #                 kwargs={"service_id": service.id})
        #     )
        # else:
        #     result = render(request, service_register_template, {"form": form})
        result = render(request, service_register_template, {"form": form})
    else:
        form = forms.CreateServiceForm()
        result = render(
            request, service_register_template, {"form": form})
    return result


def parse_catalog(request):
    if request.method == "POST":
        # form = forms.CreateServiceForm(request.POST)
        # print('PARSE CATALOG FORM')
        catalog_url = request.POST.get('url', None)
        utds = TDSCatalog(catalog_url)

        if utds.catalog_refs:
            catalog = utds.catalog_refs
            # print('CATALOG')
            data = []
            for x in utds.catalog_refs:
                # print(x)
                obj = {"name": utds.catalog_refs[x].name,
                       "href": utds.catalog_refs[x].href,
                       "title": utds.catalog_refs[x].title
                       }
                # print(obj)
                data.append(obj)

            jsonData = json.dumps(data)
            # print(jsonData)

        return JsonResponse(jsonData, safe=False, status=200)


def follow_catalog(request):
    print('FOLLOW CATALOG')
    if request.method == "POST":
        # print(request)
        request_getdata = request.POST.get('getdata', None)
        print(request_getdata)
        pid = request.POST.get('pid', None)

        try:
            utds = TDSCatalog(request_getdata)
        except Exception as e:
            return JsonResponse({"error": str(e)}, safe=False, status=500)

        data = []
        if utds.catalog_refs:
            print('CATALOG')
            # print(utds.datasets)

            for x in utds.catalog_refs:
                print(x)
                # data.append({"name": utds.catalog_refs[x].name})

                catalog = {"catalog": {"name": utds.catalog_refs[x].name,
                                       "href": utds.catalog_refs[x].href,
                                       "title": utds.catalog_refs[x].title,
                                       # "datasets": utds.datasets,
                                       }
                           }

                print(catalog)
                data.append(catalog)
                if utds.datasets:
                    for y in utds.datasets:
                        print('DATASET')
                        print(y)
                        datasets = {"datasets": {"name": utds.datasets[y].name,
                                                 "url_path": utds.datasets[y].url_path,
                                                 "access_urls": utds.datasets[y].access_urls,
                                                 # "datasets": utds.datasets,
                                                 }
                                    }
                        #
                        print(datasets)
                        data.append(datasets)

                    # jsonData = json.dumps(data)
                    # print(jsonData)
        else:
            # print(utds.datasets)
            if utds.datasets:
                for y in utds.datasets:
                    # print('DATASET')
                    # print(y)
                    datasets = {"datasets": {"name": utds.datasets[y].name,
                                             "url_path": utds.datasets[y].url_path,
                                             "access_urls": utds.datasets[y].access_urls,
                                             # "datasets": utds.datasets,
                                             }
                                }
                    #
                    # print(datasets)
                    data.append(datasets)

        return JsonResponse({"pid": pid, "data": data}, safe=False, status=200)
