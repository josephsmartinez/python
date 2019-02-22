import json
import main_function
import requests

print("")
url1 = "http://api.open-notify.org/astros.json"

astronauts_json = requests.get(url1).json()

print(astronauts_json)


astronauts = main_function.read_from_file("astronauts.json")

print(type(astronauts))

print(astronauts.keys())
