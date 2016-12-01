#! /usr/bin/env python

import os

def rename_files():
    file_list = os.listdir("/Users/bwblock/github/Udacity/python_foundations/prank")
    os.chdir("/Users/bwblock/github/Udacity/python_foundations/prank")
    for file in file_list:
        newfile = file.translate(None, "0123456789")

        print newfile


        os.rename(file,newfile)


rename_files()

