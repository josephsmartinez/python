'''
Write a Python program that given a list (example: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]), makes
a new list that has only the even elements of this list in it. This should be done in one line of code
(using list comprehension).
'''
print('Python program that given a list makes a new list that has only the even elements of this list in it')
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# the loop  and the condintional 
print([x for x in list if x % 2 == 0])