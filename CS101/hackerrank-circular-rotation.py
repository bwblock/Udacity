#!/bin/python

import sys
n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = map(int,raw_input().strip().split(' '))

old = a

r =  k % (n)
for i in range(r):
    old.insert(0,old[-1])
    old.pop()

new = old

for a0 in xrange(q):
    m = int(raw_input().strip())
    print new[m]