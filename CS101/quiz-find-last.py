# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
#! /usr/bin/env python 
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.


def find_last(search,target):

  result = -1
  end_pos = 0
  
  while True:
    start_pos = search.find(target, end_pos)
    
    if start_pos == -1:
      break
  
    result = start_pos  
    end_pos += 1
    
  return result
    
    
    
      
    
    

    
  







print find_last('aaaa', 'a')

#>>> 3

#print find_last('aaaaa', 'aa')
#>>> 3

#print find_last('aaaa', 'b')
#>>> -1

#print find_last("111111111", "1")
#>>> 8

#print find_last("222222222", "")
#>>> 9

#print find_last("", "3")
#>>> -1

#print find_last("", "")
#>>> 0




