import geocoder
import json
import requests


geoLocation = geocoder.ip("me")

latitude = geoLocation.latlng[0]
longitude = geoLocation.latlng[1]

query = input("enter query")
key = """api key"""
url = (
    "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="
    + str(latitude)
    + ","
    + str(longitude)
    + "radius=1000"
)

requestData = requests.get(url + "query=" + query + "&key=" + key)
x = requestData.json()
y = x["results"]
print(y)
