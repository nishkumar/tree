#!/usr/bin/env python3
import subprocess
import sys
import os
import re


# Function to generate sort key
# Simply convert files names to lowercase
# This way its easier to sort by ignoring case and special chars.
def get_key(s):
    return re.sub('[^A-Za-z0-9]+', '', s).lower()


# Recursive function to print file tree
def draw_tree(path, count, indent=''):
    rawList = os.listdir(path)
    fileList = []

    # Discard hidden files
    for file in rawList:
        if(not file.startswith(".")):
            fileList.append(file)

    # sort files in ascending order
    fileList = sorted(fileList, key=get_key)
    size = 0

    for fileName in fileList:
        childPath = os.path.join(path, fileName)
        # Print file name irrespective of file or dir
        size = size + 1
        if size == len(fileList):
            print(indent + "`-- " + fileName)
        else:
            print(indent + "|-- " + fileName)
        
        # If its a directory do a recursive search
        if os.path.isdir(childPath):
            count["dirs"] = count["dirs"] + 1
            if size == len(fileList):
                draw_tree(childPath, count, indent + "    ")
            else:
                draw_tree(childPath, count, indent + '|   ')
        else:
            # Is a file
            count["files"] = count["files"] + 1


# ******************************  MAIN  ******************************
# Count the number of files and dirs
count = {"files": 0, "dirs": 0}

if len(sys.argv) == 1:
    print('.')
    draw_tree('.', count)
    print()
    print('%d directories, %d files' % (count["dirs"], count["files"]))
elif len(sys.argv) == 2:
    print(sys.argv[1])
    draw_tree(sys.argv[1], count)
    print()
    print('%d directories, %d files' % (count["dirs"], count["files"]))
else:
    print('Invalid arguments! Enter a valid path.')
