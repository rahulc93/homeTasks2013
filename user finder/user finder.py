#!/usr/bin/env python

import pwd

total_list = pwd.getpwall()  # a list of all password database entries
for i in total_list:  # iterating throgh the list
    if i[5].find("home") == 1:  # if 'home' is present in the user home directory
        print i[0]  # print the user name
    if i[5].find("root") == 1:  # if 'root' is present in the user home directory
        print i[0]  # print the user name


