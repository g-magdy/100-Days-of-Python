import geocoder

my_location = geocoder.ip("me")
my_lat = my_location.geojson['features'][0]['properties']['lat']
my_lng = my_location.geojson['features'][0]['properties']['lng']