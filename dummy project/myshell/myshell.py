#!/usr/bin/env python

from cmd2 import cmd
import requests
from getpass import getuser

__version__ = '0.1'

class Application(cmd):
    """
    The main Application class
    """

    def __init__(self):
        Cmd.__init__(self)

    def do_hello(self, line):
        print 'Hello:', line

    def do_sayit(self, line):
        print 'Python rocks!'

    def do_stock(self, line):
        nasdaq = line.split(":")
        for x in nasdaq:
            url = "http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=l1" \
                % x
            value = requests.get(url).text
            if value == 0:
                print "Incorrect symbol entered- %r" % x
            else:
                print "Current share value for", x, " is", value

    def do_greet(self, line):
        print "Hello %s" % getuser()


def main():
        app = Application()
        app.cmdloop()


if __name__ == '__main__':
    main()
