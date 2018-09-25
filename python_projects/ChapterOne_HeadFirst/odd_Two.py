#Program One Python
#Joseph M.
#11/11/2017
#Program: Will determine if the current minute is odd or even.



# The name of the library and submodule.
from datetime import datetime

#Python list can hold any type of data.
odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
         21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
         41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

#Aissigns the results of the method into the variable.
#today returns a time object that contains information about the current time.
right_this_minute = datetime.today().minute


#An if statement will evaluate whether one thing is "in"side another.
#The in operator returns true or false.
if right_this_minute in odds:
    #Indentation is call suite.
    print("This minute seems a little odd.")
#Colons are a give away for a suite (block of code).
else:
    print("Not an odd minute.")

#An example using else, elif, else conditional statements.
today='Sunday'
condition='Headache'

#Level of indentation or embedded suites.
if today == 'Saturday':
    print('Party')
elif today == 'Sunday':
    if condition == 'Headache':
        print('Recover, then rest')
    else:
        print('Rest')
else:
    print('Work,work,work')


