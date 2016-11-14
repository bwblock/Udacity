#! /usr/bin/env python 
def title_case(title, minor_words):
    title_split = title.split()
    minors = []
    if minor_words:
      minors = minor_words.split()
    retitle = ''
    for e in title_split:
      if not e in minors or e == title_split[0]:
        retitle += (e[0].upper())
        if len(e) > 1:
          retitle += (e[1:].lower())
      else:
          retitle += (e.lower())
      retitle += ' '
    return retitle
              


print title_case('a clash of KINGS', 'a an the of')

