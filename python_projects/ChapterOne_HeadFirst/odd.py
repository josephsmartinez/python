#**************************************************
#Author: Joseph Martinez
#Course: HeadFirst Python
#Program: Checks if the current minute is odd or even
#Date: 11/12/2017
#**************************************************

#Import module
#There are two different ways to use the function from the imports.

#from a import f   invoke f by using f()
from datetime import datetime



#import a   invoke a.f()
import time
import random



odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
         21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
         41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]



#for loop will interate the number of times set
for i in range (5):
    
    #Assign the variable with the current minute number
    right_this_minute = datetime.today().minute

    #Conditional statements check if the current minute is odd or even
    if right_this_minute in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")

    wait_time = random.randint(1,60)
    time.sleep(wait_time)




#Using three double quotes can be used for multiline comments.
"""
Note: dir(query an object)

    Example:
    >>>dir(random)

Note: You ask the shell for help when you know the name of something.

    Example:
    >>>help(random.randint)

    Help on method randint in module random:
    
    randint(self, a, b) method of random.Random instance
        Return random integer in range [a, b], including both end points.

Note: Alt-P calls the previous typed command.

"""
