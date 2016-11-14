#! /usr/bin/env python 
x = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
y = ['c', 'd']
result = []
for i in x:
    for j in y:
        result.append( [i,j] )
print result