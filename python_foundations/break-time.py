#! /usr/bin/env python
import time
import webbrowser

print "Program started on:" + time.ctime()
tb = 3
bc = 0

while (bc < tb):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=iZhXZfZVgX0m/")
    bc += 1


