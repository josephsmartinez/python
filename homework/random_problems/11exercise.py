'''
Given a string, Write a Python program that: if the length of the string is at least 3, adds ”ing” to its
end. But, if it already ends in ”ing”, adds ”ly” instead. And if the string length is less than 3, leaves
it unchanged. Return the resulting string.
'''

def mod_string(string: str) -> str: 
  new_string= ''
  if 'ing' in string and len(string) > 3:
    new_string= string.replace('ing', 'ly')
    return new_string
  elif len(string) > 3:
    new_string= string + 'ing'
    return new_string
  else: 
    return string 

# test cases return: jumping, jumply, to
strings= ['jump','jumping','to']
print('Given a string, Write a Python program that: if the length of the string is at least 3, adds ”ing” to its end. But, if it already ends in ”ing”, adds ”ly” instead. And if the string length is less than 3, leaves it unchanged. Return the resulting string.')
print()
print('Test cases: ',  strings, ' should return:  jumping, jumply, to')
print()
for s in strings: 
  print(mod_string(s))

# s= input('Enter a word $ ')
# print(mod_string(s))

