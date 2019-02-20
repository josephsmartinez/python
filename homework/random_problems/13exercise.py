'''
Write a Python program that asks the user how many Fibonnaci numbers to generate and 
then generates them. Ask the user to enter the number of numbers in the sequence to generate.
'''
def Fibonacci(n): 
  if n<0: 
      print("Incorrect input") 
  # First Fibonacci number is 0 
  elif n==0: 
      return 0
  # Second Fibonacci number is 1 
  elif n==1: 
      return 1
  else: 
      return Fibonacci(n-1)+Fibonacci(n-2) 

user_is_fibbing = True
while user_is_fibbing:
  print('Enter Fibonnaci numbers to generate.')
  print('Press q is stop.')
  x= input('$ ')
  if x == 'q': 
    user_is_fibbing = False
  else:
    x= int(x)
    print('Fib Number: ', Fibonacci(x))