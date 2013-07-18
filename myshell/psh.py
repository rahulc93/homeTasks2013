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

    def do_hello(self, line):  # defining the 'hello' command
        print "Hello:", line  # executing the instructions for the command

    def do_sayit(self, line):  # defining the 'sayit' command
        print "Python rocks!"  # executing the instructions for the command

    def do_stock(self, line):  # defining the 'stock' command
        get_stock()  # calling the 'get_stock' method to execute the command

    def do_greet(self, line):  # defining the 'greet' command
        print_user()  # calling the 'print_user' method to execute the command


def get_stock():
    """
    This function uses the requests module and extracts the share price from the recquired URL according to the NASDAQ value given by the user
    """

     nasdaq = raw_input("Enter NASDAQ code: ")  # taking the NASDAQ code as input from the user
     url = "http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=l1" \
         % (nasdaq)  # the recquired URL from which the share price shall be obtained
     value = requests.get(url).text  # storing the share price from the URL in 'value'
     if value == 0:  # incorrect NASDAQ code provided
         print "Incorrect NASDAQ symbol."  # generate error message
     else:  # share price has been obtained
         print "The current share value is ", value  # display the value

def print_user():
    """
    This function uses the pwd module and will print the name of the user currently logged in
    """

     total_list = pwd.getpwall()  # a list of all password database entries
     for x in total_list:  # iterating through the list
         if x[5].find('home') == 1:  # the entry for the user has been found
             print "Hello %s" % x[0]  # print the user name
             break  # exit from the loop


if __name__ == '__main__':
    app = Application()
    app.cmdloop()
