#! /usr/bin/env python
import urllib

def read_text():
    quotes = open("/Users/bwblock/github/Udacity/python_foundations/movie_quotes.txt")   #creates an obect of class file.open
    contents = quotes.read()
    print contents
    check_profanity(contents)


def check_profanity(text):
    connection_object = urllib.urlopen("http://www.wdylike.appspot.com/?q=_" + text)      # creates an object of class urlopen
    output = connection_object.read()
    if "true" in output:
       print "*** Profanity detected ***"
    elif "false" in output:
       print "No profanity detected"
    connection_object.close()

read_text()
