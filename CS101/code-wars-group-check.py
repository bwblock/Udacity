#! /usr/bin/env python
def group_check(s):
  dict = {'[':5, ']':-5, '{':50, '}':-50, '(':10, ')':-10}
  sum = 0
  for e in s:
      sum += dict[e]

  return True if sum == 0 else False
  
  