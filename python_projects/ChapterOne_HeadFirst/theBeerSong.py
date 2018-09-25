#**************************************************
#Author: Joseph Martinez
#Course: HeadFirst Python
#Program: The Beer Song
#Date: 11/12/2017
#**************************************************

"""
Silly, but this program will help you understand some basic
concepts of variable, loops, and structure.
"""

word = "bottles"
for beer_num in range (99,0,-1):
    print beer_num, word, "of beer on the wall."
    print beer_num, "of beer."
    print "Take one down"
    print "Pass it around"
    if beer_num == 1:
          print "No more bottles of beer on the wall."
    else:
          new_num = beer_num - 1
          if new_num == 1:
              word = "bottle"
          print new_num, word, "of beer on the wall."
    print

"""
Help on built-in function range in module __builtin__:

range(...)
    range(stop) -> list of integers
    range(start, stop[, step]) -> list of integers
    
    Return a list containing an arithmetic progression of integers.
    range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
    When step is given, it specifies the increment (or decrement).
    For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
    These are exactly the valid indices for a list of 4 elements.
"""
