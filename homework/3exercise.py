# return {1:1, 2: 4, 3: 9}
x = input("Enter a number: ")
my_list = {}

for x in range(1, x+1):
  my_list.update({x: (x*x)})

print(my_list)
