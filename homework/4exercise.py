
person = {}
age = 35
name = "Mike"

person.update(
  {
  'name': name,
  'age': age
  }
)

old_age = 100 - person['age']

print("Hello {}, you will be 100 in {} years!".format(name, old_age))