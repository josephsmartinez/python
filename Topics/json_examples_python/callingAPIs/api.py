import json, requests



url="https://maps.googleapis.com/maps/api/staticmap?center=40.714%2c%20-73.998&zoom=12&size=400x400&key="
key="AIzaSyB6V3Ut60fkvrA-wp_9XgQreUiEDvMlfaU"

url_key= url+key

reponse = requests.get(url_key)

print(reponse.status_code)

print(reponse.content)

'''
Resources: 
https://developers.google.com/maps/documentation/maps-static/get-api-key
'''