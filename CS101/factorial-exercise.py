#! /usr/bin/env python 
import math

def permutations(n,k):

#  permutations of n items placed in k places i.e. n people placed in k chairs ----  nPk

    if k > n:
      return False
    return math.factorial(n) / math.factorial(n-k)
    
    
    
def combinations(n,k):

# combinations of k items chosen from a pool of n --- i.e. n people placed in 4 chairs ----  nCk
    if k > n:
      return False
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k)) * 1.0
    

def ft_prob_at_least(makes,total_shots,ftp):

# probability of at LEAST makes number of free throws given total_shots and ftp free throw percentage as a fraction
    i = makes
    p = 0
    while i <= total_shots:
      p += ftp**i * (1 - ftp)**(total_shots - i) * combinations(total_shots, i)
      i += 1
    
    return p
    
def ft_prob(makes,total_shots,ftp):

# probability of EXACTLY makes number of free throws given total_shots and ftp free throw percentage as a fraction

      return(ftp**makes * (1 - ftp)**(total_shots - makes) * combinations(total_shots, makes))

print combinations(56,5) 


print ft_prob(3,3, .714)