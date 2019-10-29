from flask import Flask, render_template, render_template_string, request, make_response
from aqiProject import google_api, aqi_api, json_to_xml
from fileio import FileIO

app = Flask(__name__)
app.config['SECRET_KEY'] = '6dfed37d10b6d7034c0ebbb2972bd97d'

@app.route('/')
def home():

    # Run new image per request to route
    lat_long=aqi_api()
    google_api(lat_long)
    aqi_json = FileIO.read_jsonfile('aqi.json')
    return render_template('index.html', lat_long=lat_long, aqi_json=aqi_json)

@app.route('/xml')
def xml():
  json_to_xml()
  return render_template('aqi.xml')

if __name__== '__main__':
  # host is default to localhost
  app.run(debug=True,host='0.0.0.0', port=8080)