#lambda function in python - used to create anonymous function objects
#example 1
x = lambda a : a + 10
print(x(5))

#############################################
#example 2
x = lambda a, b : a * b
print(x(5, 6))

#############################################
#example 3
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#############################################
#example 4
def foo(n):
  return lambda a : a * n

doubler = foo(2)

print(doubler(11))

mytripler = foo(3)

print(mytripler(11))

#############################################
#example 5
list1=[1,2,3]
list2=[4,5,6]

#creating a function to multiply two lists:
multiply_list_fun=lambda x,y:x*y

#printing its type to confirm that it is a function:
print(type(multiply_list_fun))

#multiplying pairs of element from both lists - list1 and list2
mapping=map(multiply_list_fun,list1,list2)

#transforming the result into a list:
list3=list(mapping)

#printing the result:
print(list3)

#redoing the last 5 lines of code in one only line:
print(list(map(lambda x,y:x*y,list1,list2)))