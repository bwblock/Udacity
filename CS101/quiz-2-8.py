# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.


def biggest(a,b,c):
    if a > b:
      big = a
    else:
      big = b
    if big > c:
      return big
    else:
      return c
      
      


#print biggest(3, 6, 9)
#>>> 9

#print biggest(6, 9, 3)
#>>> 9

#print biggest(9, 3, 6)
#>>> 9

#print biggest(3, 3, 9)
#>>> 9

#print biggest(9, 3, 9)
#>>> 9