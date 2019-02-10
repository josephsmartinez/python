'''
Given 2 lists, a and b, containing integers, not necessarily with the same length, Write a Python
program that returns a list that contains only the elements that are common between the lists a and
b (without duplicates).
'''
print('Python program that returns a list that contains only the elements that are common between the lists a and b (without duplicates).')
a = {1,2,3,4,5,6,7,8,9}
b = {5,2,4,6}
print('List A: ', a)
print('List B: ', b)
new_list = a.intersection(b)
print('New List C: ', new_list)