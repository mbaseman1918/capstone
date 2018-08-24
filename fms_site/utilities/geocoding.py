import requests
from utilities.secrets import GeoCoding_API
from fmsapp.models import Address
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

def get_user_lat_lng(request):
    current_user = get_object_or_404(User, username='newuser')
    targ_address = get_object_or_404(Address, user=current_user)
    physical_address = targ_address.street_address+',+'+targ_address.city+',+'+targ_address.state
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+physical_address+'&key='+GeoCoding_API
    response = requests.get(url)
    data = response.json()
    lat_lng = data['results'][0]['geometry']['location']
    return lat_lng
