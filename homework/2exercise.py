
def fact(x):
  if x <= 0:
    return 1
  else:
    return (x * fact(x-1))

# print(fact(5))

x = input("enter int number for factoral: ")
print(fact(int(x)))
