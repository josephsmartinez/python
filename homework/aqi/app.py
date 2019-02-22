from flask import Flask, render_template, render_template_string, request
from aqiProject import google_api, aqi_api
from fileio import FileIO

app = Flask(__name__)
app.config['SECRET_KEY'] = '6dfed37d10b6d7034c0ebbb2972bd97d'

@app.route('/')
def index():

    # Run new image per request to route
    lat_long=aqi_api()
    google_api(lat_long)
    aqi_json = FileIO.read_from_file('aqi.json')
    return render_template('index.html', lat_long=lat_long, aqi_json=aqi_json)


if __name__== '__main__':
  # host is default to localhost
  app.run(host="piggy.ad.fiu.edu",debug=True, port=3000)