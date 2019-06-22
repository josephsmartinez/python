# Template Strings
# https://docs.python.org/3.4/library/string.html#template-strings

from string import Template

def main():
  # Example1 : Usual string formatting with format()
  str1 = "You're watching {0} by {1}".format("Advanced Python", "Joe Mart")
  print(str1)

  # Exmaple 2: Create a template with placeholders
  templ = Template("You're watching ${title} by ${author}")

  # use the substitute method with keyword arguments
  str2 = templ.substitute(title="Advanced Python", author="Joe Mart")
  print(str2)

  # Exmaple 3: notice the difference with the place holders
  templ = Template('Hello $first_name $last_name, welcome to $place')
  str3 = templ.substitute(first_name='Joe', last_name='Mart', place='IHOP')
  print(str3)

  # use the substitute method with a dictionary
  data = { 
      "first_name": "Joe Marini",
      "last_name": "Advanced Python",
      "place": "Denny's"
  }
  str3 = templ.substitute(data)    
  print(str3)

if __name__ == "__main__":
  main()