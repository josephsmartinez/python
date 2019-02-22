#based on the JSON material from MDN web docs (available at: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
#learn how to read from a JSON file in Python
#importing necessary libraries
import json

#opening json files
with open("superheroes.json", "r") as read_file:
    sch = json.load(read_file)

#printing the type of the file
print(type(sch))

#printing its keys
print(sch.keys())

#sch["members"] is a list of dictionaries such that each dictionary contains the information of each supehero
#for each element of the list, we are printing the strength of each member
for x in sch["members"]:
    print(x["strength"])

#formatting the string to be printed given the name and the strength of each superhero
for x in sch["members"]:
    print("{0} has strength {1}".format(x["name"],x["strength"]))

#printing all members
print(sch["members"])

#printing all members but in ascending order of strength
print(sorted(sch["members"],key=lambda k : k["strength"]))


