#! /usr/bin/env python 



from ggplot import *
print (ggplot(diamonds, aes(x='price', color='cut')) + \
geom_density())