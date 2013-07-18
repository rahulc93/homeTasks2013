myshellv1
=========

In this assignment. we will create a virtualenv and run this script which will create a small shell like environment with 'Cmd' as prompt, and where we can give some commands to it.

Source
------

The code for the problem can be found `here <https://github.com/rahulc93/homeTasks2013/blob/master/myshell/psh.py>`_

Solution
--------

The solution to the above problem is given below.

.. code:: python
    
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
	    nasdaq = raw_input("Enter NASDAQ code: ")  # taking the NASDAQ code as input from the user
	    url = "http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=l1" \
		% (nasdaq)  # the recquired URL from which the share price shall be obtained
	    value = requests.get(url).text  # storing the share price from the URL in 'value'
	    if value == 0:  # incorrect NASDAQ code provided
	    print "Incorrect NASDAQ symbol."  # generate error message
	    else:  # share price has been obtained
		print "The current share value is ", value  # display the value

	def do_greet(self, line):  # defining the 'greet' command
	    total_list = pwd.getpwall()  # a list of all password database entries
	    for x in total_list:  # iterating through the list
		if x[5].find('home') == 1:  # the entry for the user has been found
		    print "Hello %s" % x[0]  # print the user name
		    break  # exit from the loop



      if __name__ == '__main__':
	app = Application()
	app.cmdloop()

Run the program
---------------

To run the program, save it as *psh.py*, and::

    $ python psh.py


