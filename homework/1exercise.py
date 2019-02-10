'''
Write a Python program that finds all numbers that are divisible by 7 but not a multiple of 5 between
2000 and 3201 (included).
'''
print('Python program that finds all numbers that are divisible by 7 but not a multiple of 5 between 2000 and 3201 (included).')
#x = input("please enter a number")
x = 100
numbers = []
for x in range (0,x):
  if x % 7 == 0 and x % 5 != 0:
    numbers.append(x)
print(numbers)
