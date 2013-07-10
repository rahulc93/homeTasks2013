#!/usr/bin/env python
fl = open("/proc/mounts") # open the file /proc/mount
for line in fl: # loop through the lines in the file
    print line, # print a line from the file in each loop
    fl.close() # close the file /proc/mounts
