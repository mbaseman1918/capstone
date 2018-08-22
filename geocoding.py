from fms_site.utilities.secrets import GeoCoding_API
import requests

response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=5152+Linn+Lane,+West+Linn,+OR&key='+GeoCoding_API)
data = response.json()
print(data['results'][0]['geometry']['location'])
