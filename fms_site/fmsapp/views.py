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

# def add_address(request):
#     if request.method == "POST":
#         new_user = request.user
#         new_street_address = request.POST['street_address']
#         new_city = request.POST['city']
#         new_state = request.POST['state']
#         new_address = Address(user=new_user, street_address=new_street_address, city=new_city, state=new_state)
#         new_address.save()
#     return HttpResponseRedirect(reverse('fmsapp:index'))

def delete_address(request):
    pass

def compare_address(request):
    pass

def display_address_on_map(request):
    lat_lng = get_user_lat_lng(request)
    lat = lat_lng['lat']
    lng = lat_lng['lng']
    print(lat_lng)
    print(lat)
    print(lng)
    # return HttpResponse(lat_lng['lat'])
    map_src = "https://maps.googleapis.com/maps/api/js?key="+GeoCoding_API+"&callback=initMap"
    context = {
    'map_user':map_src,
    'lat':lat,
    'lng':lng,
    }
    return render(request, 'fmsapp/map.html', context)
