#! /usr/bin/env python 
def alphabet_position(text):
    key = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for e in text:
      if e.lower() in key:
        result += str(key.index(e.lower())+1)
        result += ' '

    result = result.rstrip()
    return result

 



def alp_position(text):
   return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
   
   
     
print alp_position('a test')