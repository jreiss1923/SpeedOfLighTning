import requests
import json

url = "https://maps.googleapis.com/maps/api/directions/json?origin=place_id:ChIJmSybOxd644kRj0V_-AgTGd8&destination=place_id:ChIJXdNMUiJ644kR4_Jn8xLhIPg&mode=walking&key=" + g_maps_key

response = requests.get(url, headers={}, data={})
print(json.loads(response.text)['routes'][0]['legs'][0]['duration']['value'])