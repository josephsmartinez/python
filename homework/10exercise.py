'''
Given a number n (user input), Write a Python program to determine if n is a prime.
'''

def prime(number: int) -> bool:
  '''
  Assume not prime until proven
  '''
  prime= False
  for i in range(2,10):
    # Check for numbers < 10 
    prime_singles = [1,2,3,5,7]
    if number in prime_singles:
      prime=True
      break
    # Check for numbers > 10 
    if number % i == 0: 
      prime= False
      break
    else:
      prime=True
  return prime

# Print if prime or not prime
print('Python program to determine if n is a prime.')
number= int(input('Enter a number: $ '))
if prime(number):
  print('number: ', number, 'is prime')
else: 
  print('number: ', number, 'is not prime')