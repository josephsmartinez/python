'''
Write a Python program to sum all the values (not keys) in a dictionary.
'''
print('Python program to sum all the values (not keys) in a dictionary.')
dic = {'0': 400, '1': 600}
print('Dictionary: ', dic)
sum = 0
for x in dic:
  sum = sum + dic[x] 
print('Sum for vaules: ', sum)