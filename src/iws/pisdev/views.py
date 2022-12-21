import json

from django.shortcuts import render

# Create your views here.


import logging

from django.shortcuts import render
from django.utils.translation import ugettext as _


logger = logging.getLogger(__name__)
master = {}


def index(request):
  print('-- pisdev dajngo-app index --')
  return render(request, 'app.html')
