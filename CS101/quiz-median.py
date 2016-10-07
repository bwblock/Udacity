#! /usr/bin/env python 
# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):

	big1 = bigger(a,b)
	big2 = bigger(b,c)
	big3 = bigger(a,c)
	
	max = biggest(a,b,c)
	if big1 == big2:
	  return big3
	if max == big1:
	  return big2
	else:
	  return big1
	









print(median(1,3,2))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7







