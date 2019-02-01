
#x = input("please enter a number")
x = 100
numbers = []

for x in range (0,x):
  if x % 7 == 0 and x % 5 != 0:
    numbers.append(x)

print(numbers)
