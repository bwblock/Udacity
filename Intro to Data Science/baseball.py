#!/usr/bin/env python
import numpy
import scipy.stats
import pandas

def compare_averages(filename):
    """
    Performs a t-test on two sets of baseball data (left-handed and right-handed hitters).

    Source data is a csv file that has three columns.  A player's
    name, handedness (L for lefthanded or R for righthanded) and their
    career batting average (called 'avg').  
    
    Function reads the csv file into a pandas data frame,
    and runs Welch's t-test on the two cohorts defined by handedness.
    
    One cohort is a data frame of right-handed batters. And the other
    cohort is a data frame of left-handed batters.=
    
    With a significance level of 95%, if there is no difference
    between the two cohorts, function return a tuple consisting of
    True, and then the tuple returned by scipy.stats.ttest.  
    
    If there is a difference, return a tuple consisting of
    False, and then the tuple returned by scipy.stats.ttest.
    
    """

baseball_stats = pandas.read_csv('baseball_stats.csv')

left_hand = baseball_stats[baseball_stats.handedness == 'L']

right_hand = baseball_stats[baseball_stats.handedness == 'R']

left_average = left_hand['avg']
right_average = right_hand['avg']

print numpy.average(right_average)
print numpy.average(left_average)

test = scipy.stats.ttest_ind(left_average,right_average,equal_var=False)

if (test[1]) <= 0.05:	
	same = False
elif (test[1]) > 0.05:
	same = True
	
result = same, test[0], test[1]

print result



