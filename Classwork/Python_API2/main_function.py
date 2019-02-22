import json

def read_from_file(file: str) -> dict:
  with open(file, "r") as read_file:
    json.load(read_file)
    print("file read".format(file))
    return file

def write_to_file(file):
  with open(file, "w") as write_file:
    json.dump(data, write_file, indent=2)
    print("The {0} file was created")

'''
another boring class...zzzzzz 
'''