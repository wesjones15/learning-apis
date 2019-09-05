import httplib2
import json

def getGeocodeLocation(inputString):
    google_api_key = "AIzaSyAMW2M0uVpA5CL6tKfSQH7_S5UInoWY_y0"
    location_string = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (location_string, google_api_key))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)
    return result

result = getGeocodeLocation('Downingtown, Pennsylvania')
print (result['results'][0]['formatted_address'])
location = result['results'][0]['geometry']['location']
print (location['lat'], location['lng'])
