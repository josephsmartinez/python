
# define a function that takes variable arguments
def addition(base, *args):
    result = 0
    for arg in args:
        result += arg

    return result

def myFun(**kwargs):  
    for key, value in kwargs.items(): 
        print("%s == %s" %(key, value))

def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

def main():
    # pass different arguments
    print(addition(5, 10, 15, 20))
    print(addition(1, 2, 3))

    # pass an existing list
    myNums = [5, 10, 15, 20]
    print(addition(*myNums))

    # **kwargs, it allows us to pass the variable length of keyword arguments to the function.
    myFun(first ='Geeks', mid ='for', last='Geeks')
    intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
    intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)    

if __name__ == "__main__":
    main()