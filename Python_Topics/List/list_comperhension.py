# As list comprehension returns list, they consists of brackets containing the expression which needs to be executed for each element along with the for loop to iterate over each element
# Basic syntax:
# new_list = [expression for_loop_one_or_more condtions]

comp_list = [x for x in range(0,10)]
print(comp_list)

evens_list = [x for x in range(0,10,2)]
print(evens_list)

inter_list = [1,2,3,4,5,6,7,8,9]
one_to_ten = [i for i in inter_list]
print(one_to_ten)

squares = [n**2 for n in inter_list]
print(squares) 