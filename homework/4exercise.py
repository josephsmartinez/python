'''
Write a Python program that asks the user for their name and their age. Then, print out a message
telling them the year that they will turn (or turned) 100 years old.
'''
person = {}
name = input('Please enter your name $ ')
age = int(input('Please enter your age $ '))
# age = 35
# name = "Mike"
person.update(
  {
  'name': name,
  'age': age
  }
)
old_age = 100 - person['age']
print("Hello {}, you will be 100 in {} years!".format(name, old_age))