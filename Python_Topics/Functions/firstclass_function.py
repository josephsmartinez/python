# First-class functions:
# "A programming language is said to have first-class function if it treats functions as first-class citizens"

# First-class citizen (programming):
# "An entity which supports all the operations generally available to tother entities. 
# There operation typically include being passed as an argument, returned form a function, and assigned to a variable."

# https://www.youtube.com/watch?v=kr0mpwqttM0

def square(x):
    return x * x

# Common function call
f = square(5)
print(f)

# We can assign the varaible with a function
f = square
print(f(5))

def cube(x):
    return x * x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

cube_list = my_map(cube, list(range(0,10)) )
print(cube_list)
