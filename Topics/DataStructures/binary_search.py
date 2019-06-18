import random

def bubbleSort(numbers):
  pass

def binarySearch(numbers, x):
  mid= int(len(numbers)-1/2)
  print(mid)
  if x == numbers[mid]:
    return numbers[mid]
  if x < numbers[mid]:
    numbers=numbers[0:mid]
    return binarySearch(numbers, x)
  else:
    numbers=numbers[mid:]
    return binarySearch(numbers, x)
  return 1

if __name__ == "__main__":
  numbers=[]
  for i in range(0,1000):
    numbers.append(random.randint(1,100))
    #bubbleSort()
    num=[1,2,3,4,5,6]
    binarySearch(num, 3)