import phonenumbers
import folium
from mynumber import number
from phonenumbers import geocoder
key= "d8bb3ce036fe47faab3b603b274110bb"
sanNumber = phonenumbers.parse(number)#parse is used to convert the string datatype into another datatype
yourLocation = geocoder.description_for_number(sanNumber,"en")#for language provider
print(yourLocation)
## get service provider
from phonenumbers import carrier# it is used for last update information
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))
from opencage.geocoder import OpenCageGeocode
geocoder =OpenCageGeocode(key)
query = str(yourLocation)
results = geocoder.geocode(query)
##print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)
myMap = folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=yourLocation).add_to((myMap))
myMap.save("myLocation.html")

