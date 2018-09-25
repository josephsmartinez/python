"""
**************************************************
Author:     Joseph Martinez
Course:     HeadFirst Python
Program:    Experimenting with ranges
Date:       11/12/2017
**************************************************
"""
print "(start, stop, step)\n"

print "Output of range(5)\n", range(5)
print

print "list(range(5))\n", list(range(5))
print

print "list(range(0, 10, 2))\n", list(range(0, 10, 2))
print

print "list(range(10, 0, -2))\n", list(range(10, 0, -2))
print

#Be careful Python wont let you make a list when your index range is shorter than the start.
print "list (range(10, 0, 2))\n", list (range(10, 0, 2))
print

print "list(range(99, 0, -1))\n", list(range(99, 0, -1))
print
     
"""
range(...)
    range(stop) -> list of integers
    range(start, stop[, step]) -> list of integers
    
    Return a list containing an arithmetic progression of integers.
    range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
    When step is given, it specifies the increment (or decrement).
    For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
    These are exactly the valid indices for a list of 4 elements.
"""
