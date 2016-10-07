#! /usr/bin/env python 

def get_page(url): 
		try: 
		  import urllib 
		  return urllib.urlopen(url).read()
		except:
		  return ""

print get_page('http://xkcd.com/353')

