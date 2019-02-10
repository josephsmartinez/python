'''
Write a Python program that generates a dictionary with the format i : i ∗ i given a certain integer
number n (input by the user). For instance, if the user inputs 3, then the dictionary should have the
following format: 1: 1, 2: 4, 3: 9.
'''
print('Python program that generates a dictionary with the format i : i ∗ i given a certain integer number n (input by the user).')
# return {1:1, 2: 4, 3: 9}
x = int(input("Enter a number: "))
my_list = {}
for x in range(1, x+1):
  my_list.update({x: (x*x)})
print(my_list)
