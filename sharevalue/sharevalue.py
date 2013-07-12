#!/usr/bin/env python

import urllib2
import sys

def get_value(nasdaq):
    """
    This function fetches the current share value according to the NASDAQ code given by the user and displays it.

    :arg nasdaq: NASDAQ code given by the user
    """
    
    link = 'http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=l1' % (nasdaq)  # store the recquired URL acording to the NASDAQ value in the 'link' variable
    link_open = urllib2.urlopen(link)  # opening the URL
    price =  float(link_open.read())  # store the value retrieved from the URL in the 'price' variable
    if price == 0.00:  # incorrect NASDAQ value given by user
        print 'The NADAQ code entered is wrong. '  # display an error message
    else:
        print 'The latest share value is %s' % (price)  # display the value obtained from the URL
        
def main(nasdaq):
    """
    This function recieves the NASDAQ code and calls the desired function to fetch the current share value.

    :arg nasdaq: NASDAQ code given by the user
    """

    get_value(sys.argv[1])  # calls the 'get_value' method, passing to it the first command line parameter as argument


if len(sys.argv) != 2:  # incorrect syntax for executing the program from command line
    print 'Wrong syntax. '  # display error message
    sys.exit(-1)  # abnormal termination
else:  #syntax is ok
    main(sys.argv[1])  # pass the NASDAQ code to main given by user
sys.exit(0)  # successful termination

