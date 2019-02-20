'''
Write a Python program that asks the user for a certain number and then prints out a list of all the
divisors of that number.
'''
print('Python program that asks the user for a certain number and then prints out a list of all the divisors of that number.')
number = int(input('Please enter a number $ '))
#number = 20
# 1, 2, 4, 5, 10, 20
for x in range(1, number+1):
  if number % x == 0:
    print(x)