'''
Write a Python program that calculates the moment (year, month and day) when someone has lived for 10^9 seconds.
Reference: Adding Dates and Times in Python http://www.pressthered.com/adding_dates_and_times_in_python/
'''
import datetime  

def live_for_10pow9(year: int, month: int, day: int) -> str:
  '''
  Using the built-in modules datetime and timedelta, you can perform date and time addition/subtraction
  '''
  flag = 10**9
  mydate = datetime.datetime(year, month, day) + datetime.timedelta(seconds=flag)
  return mydate

print('Python program that calculates the moment (year, month and day) when someone has lived for 10^9 seconds.')
month = int(input('Please enter your birth month $ '))
day = int(input('Please enter your birth day $ '))
year = int(input('Please enter your birth year $ '))
newdate = live_for_10pow9(year, month, day)
print('You will have lived for 10^9 seconds by: ', newdate)
