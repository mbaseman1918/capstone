from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.urls import reverse
from .models import Address
from utilities.secrets import GeoCoding_API
from utilities.geocoding import get_user_lat_lng
from utilities.firmsdatagrab import get_fire_data

# Create your views here.

def index(request):
    if User.is_authenticated:
        context = {
        'user':request.user,
        }
    return render(request,'fmsapp/index.html', context)



def compare_address(request):
    pass

def display_address_on_map(request):
    fire_list = get_fire_data()
    fire_lat = []
    fire_lng = []
    for i in fire_list[1:]:
        fire_lat.append(float(i['lat']))
        fire_lng.append(float(i['lng']))
    user_lat_lng = get_user_lat_lng(request)
    user_lat = user_lat_lng['lat']
    user_lng = user_lat_lng['lng']
    map_src = "https://maps.googleapis.com/maps/api/js?key="+GeoCoding_API+"&libraries=visualization&callback=initMap"
    context = {
    'map_user':map_src,
    'user_lat':user_lat,
    'user_lng':user_lng,
    'fire_lat':fire_lat,
    'fire_lng':fire_lng,
    }
    return render(request, 'fmsapp/map.html', context)
