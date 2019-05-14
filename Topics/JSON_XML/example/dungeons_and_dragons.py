#learn how to save an object from Python into JSON
#based on the work of Lucas Lofaro (available at: https://realpython.com/python-json/)
import json

#defining our class
class Elf(object):
    def __init__(self,level,ability_scores=None):
        self.level=level
        self.ability_scores={
            "str":11, "dex":12, "con":10,
            "int":16, "wis":14, "cha":13
        } if ability_scores is None else ability_scores
        self.hp=10 + self.ability_scores["con"]

#creating an object passing both arguments, level and ability_scores
gregelf=Elf('first_level',{
    "str":12, "dex":8, "con":20,
    "int":14, "wis":12, "cha":17
    })

#printing this objects's hp
print(gregelf.hp)

#creating an object passing only one argument, level
zelda=Elf('second_level')

#printing this second objects's hp
print(zelda.hp)

#accessing one of its attributes
print(zelda.level)

#transforming the first object into a dictionary
gregelfDict = gregelf.__dict__

#printing its type to confirm that it is a dictionary
print(type(gregelfDict))

#saving this dictionary into a jsson file with indentation 4
with open('elf_files.json','w') as write_file:
    json.dump(gregelfDict,write_file,indent=4)

