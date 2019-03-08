# API call methods
# V 0.0.1
# Add OS to append files to relitve paths

import json, requests, googlemaps
from fileio import FileIO
from os import path
from json2xml import json2xml, readfromurl, readfromstring, readfromjson

def aqi_api(api_key=None,url=None) -> dict:
  '''
  Air Quality Programmatic APIs
  '''

  if api_key == None and url == None:
    # API Key and URL Default
    api_key = FileIO.read_from_file('api_key.json')
    url="http://api.airvisual.com/v2/nearest_city?key="
    url_aqi=url+api_key['iqair']

  try:
    # Call API
    response = requests.get(url_aqi)
    FileIO.log(str(response.json()), str(type(response.json())))
    request_json = response.json()

    # Handle Bad Request or Process 
    if response.status_code == requests.codes.ok:
      aqi_json_file_name="aqi.json"
      FileIO.save_to_file(request_json, aqi_json_file_name)

      air_quality_index= FileIO.read_from_file(aqi_json_file_name)
      #print("Pollution data", air_quality_index['data']['current']['pollution'])
      FileIO.log("Pollution data", str(air_quality_index['data']['current']['pollution']))

      latitude= air_quality_index['data']['location']['coordinates'][0]
      longitude= air_quality_index['data']['location']['coordinates'][1]
      #print('latitude: ' + str(latitude), 'longitude: ' + str(longitude))
      FileIO.log('latitude: ' + str(latitude), 'longitude: ' + str(longitude))

  except Exception as e:
    print('error with request processing!', e)
    FileIO.log('error with request processing!', e)
  
  lat_lon = {'latitude': str(latitude),'longitude': str(longitude)}
  return lat_lon

def google_api(lat_lon: dict) -> bool:
  '''
  Google Maps API
  Makes a .png file
  '''
  # URL Parameters 
  google_map_created = False
  params= "center={0},{1}&zoom=12&scale=1&size=600x300&maptype=roadmap&key=AIzaSyB6V3Ut60fkvrA-wp_9XgQreUiEDvMlfaU&format=png&visual_refresh=true&markers=size:mid%7Ccolor:0xff0000%7Clabel:1%7C{2},{3}".format(lat_lon['longitude'],lat_lon['latitude'],lat_lon['longitude'],lat_lon['latitude'])
  url_google_maps="https://maps.googleapis.com/maps/api/staticmap?" + params

  try:
    # Call API
    response = requests.get(url_google_maps)
    
    # Handle Bad Request or Process 
    if response.status_code == requests.codes.ok:
      FileIO.log("google request: ", str(response.status_code), "object type: ", response.headers.get('content-type'))
      open('city.png', 'wb').write(response.content)

      google_map_created = True

  except Exception as e:
    print('error with request processing!', e)
    FileIO.log('error with request processing!', e)
    google_map_created = False
  
  return google_map_created

def json_to_xml() -> bool:
  '''
  Converts json to xml
  return -> boolean
  '''

  # Data should be written appended to a file with correct xml header 
  # An xsl file should have all html/css stlying to render data from xml

  data = readfromjson("aqi.json")
  print(json2xml.Json2xml(data).to_xml())

if __name__ == '__main__':
    lat_lon = aqi_api()
    google_map_created = google_api(lat_lon)
    json_to_xml()
    if google_map_created:
      print("google image created!")
    

''' 
- In aqiProject.py, read your api key from the json file you created above and assign it to a variable named my aqi api key
- Continuing aqiProject.py, define the following variables
- Continuing aqiProject.py, define the following variables
- Now make a request to this API and save the output to variable aqi json
- Save this data into a json file. For this, create a name for the json file
- Read the data from the json file that we just created and save to a variable
- In the json file that you saved, you have the latitude and longitude of the location 
  from which you collected the air quality information. Save these values in two variables
    - latitude
    - longitude
- Copy these values of latitude and longitude; visit Google Maps; paste and search 
  this exact location; take a screen shot of the location. 
- Save this image in the PyCharm’s project folder with name city.png (you might use other image formats).
'''

''' 
References: 
http://docs.python-requests.org/en/master/user/quickstart/#response-status-codes
https://github.com/googlemaps/google-maps-services-python'
https://developers.google.com/maps/documentation/maps-static/dev-guide
https://www.codementor.io/aviaryan/downloading-files-from-urls-in-python-77q3bs0un
'''