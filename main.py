import phonenumbers
from test import number

from phonenumbers import geocoder
ch_number = phonenumbers.parse(number, "CH")

#IN BELOW LINE YOU WILL COUNTRY LOCATION OF PHONENUMBER
print("1.This is your country:\n")
print(geocoder.description_for_number(ch_number,"en"))
print("--------------------------------------------------------------------------------------------")

#NOW LETS ALSO FIND THE SERVICE PROVIDER OF THIS PHONE NUMBER

from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print("2.This is your Service Provider:\n")
print(carrier.name_for_number(service_number, "en"))
print("----------------------------------------------------------------------------------------------")


#LETS FIND THE TIMEZONE NOW
from phonenumbers import timezone
gb_number = phonenumbers.parse(number, "GB")

print("3.This is your Timezone:\n")
print(timezone.time_zones_for_number(gb_number))
print("----------------------------------------------------------------------------------------------")




# # Lat and Long from GPS
# # import geocoder

# # g = geocoder.ip(ip_)
# # w = g.latlng
# # print(w)




# #IP ADDDRESS LOCATOR
# import requests
# import urllib
# import urllib.request
# import json

# ip_address = ''
# request_url = 'https://geolocation-db.com/jsonp/' + ip_address
# response = requests.get(request_url)
# result = response.content.decode()
# result = result.split("(")[1].strip(")")
# result  = json.loads(result)
# # print(result)




# # Import module Long and Lat to Location
# from geopy.geocoders import Nominatim

# # Initialize Nominatim API
# geolocator = Nominatim(user_agent="geoapiExercises")




# # https://www.iplocation.net/ip-lookup

# # Assign Latitude & Longitude

# Latitude = 25.0478
# Longitude = 121.5318

# # Dsiaplying Latitude and Longitude
# print("Latitude: ", Latitude)
# print("Longitude: ", Longitude)

# # Get location with geocode
# sent = f'{Latitude} , {Longitude}'
# location = geolocator.geocode(sent)

# # Dsiplay location
# # print("\nLocation of the given Latitude and Longitude:")
# print(location)

