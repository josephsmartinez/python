'''
Write a Python program that implement a function that takes as input three variables, and returns
the largest of the three. Do this without using the Python max() function! Hint: Use if statements.
'''

# RUN TIME: O(N)
def max(numbers: list) -> int:
  '''
  Find max value
  Return 0 if list empty
  '''
  if len(numbers) == 0: 
    return 0
  elif len(numbers) == 1:
    return numbers[0]

  max=0
  for i in range(0,len(numbers)-1):
    if numbers[i] > numbers[i+1]:
      max = numbers[i]
  return max

numbers = [-1, 10, -3]
print(numbers)
print(max(numbers))

