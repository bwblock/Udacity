# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.


def measure_udacity(p):
    result = 0
    for e in p:
      if e[0] == 'U':
        result += 1
    return result
        


print (measure_udacity(['Dave','Sebastian','Katy']))
#>>> 0

#print measure_udacity(['Umika','Umberto'])
#>>> 2