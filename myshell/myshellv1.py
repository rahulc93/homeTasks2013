from cmd2 import Cmd
import requests
import pwd

__version__ = '0.1'

class Application(Cmd):
    """
   The main Application class
   """

    def __init__(self):
        Cmd.__init__(self)

    def do_hello(self, line):
        print "Hello:", line

    def do_sayit(self, line):
        print "Python rocks!"

    def do_stock(self, line):
        get_stock()

    def do_greet(self, line):
        print_user()


def get_stock():
    nasdaq = raw_input("Enter NASDAQ code: ")
    url = "http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=l1" \
        % (nasdaq)
    value = requests.get(url).text
    if value == 0:
        print "Incorrect NASDAQ symbol."
    else:
        print "The current share value is ", value

def print_user():
    total_list = pwd.getpwall()
    for x in total_list:
        if x[5].find('home') == 1:
            print "Hello %s" % x[0]


if __name__ == '__main__':
    app = Application()
    app.cmdloop()
