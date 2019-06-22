# Decorators

# Quick recap on closure
def outer_function(msg): 
    message = msg

    def inner_function():
        print(message)
    return inner_function

hi_func = outer_function('Hi')
bye_func = outer_function('Bye')

hi_func()
bye_func()

# EXAMPLE
# We can wrap the orignal function to add more functionality
print('\n\nExample 1 ####')

def decorator_function(original_function): 
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__) + '()')
        return original_function()
    return wrapper_function

# # Orginal Function
# def display():
#     print('display() function ran')

# New Function
@decorator_function
def display():
    print('display() function ran')

#decorated_display = decorator_function(display)
#decorated_display()
display()


# EXAMPLE 2
print('\n\nExample 2 ####')

def decorator_function2(original_function):
    def wrapper_function2(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__) + '()')
        return original_function(*args, **kwargs)
    return wrapper_function2

@decorator_function2
def display2():
    print('display2 function ran')

@decorator_function2
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 25)

display2()
