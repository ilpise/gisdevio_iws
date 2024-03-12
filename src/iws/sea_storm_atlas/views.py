from django.shortcuts import render, redirect

from .models import SeaStormAtlasConfiguration

def index(request):
  print('-- sea_storm_atlas python package index --')
  return render(request, 'sea_storm_atlas/app.html')


def redirect_to_map(request):
  conf = SeaStormAtlasConfiguration.objects.get()
  print('-- redirect_to_map --')
  print(conf)
  return redirect(f'/catalogue/#/map/{conf.map}')
