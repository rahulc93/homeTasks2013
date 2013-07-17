user finder
===========

In this assignment, we write a program which will return a list of all users present in the system who can do a proper login.

Source Code
-----------

The code for the above problem can be found `here <https://github.com/rahulc93/homeTasks2013/blob/master/user%20finder/user%20finder.py>`_

Solution
--------

Here is the solution to the problem

.. code:: python

    !/usr/bin/env python
 
    import pwd
  
    total_list = pwd.getpwall()  # a list of all password database entries
    for i in total_list:  # iterating throgh the list
        if i[5].find("home") == 1:  # if 'home' is present in the user home directory
            print i[0]  # print the user name
        if i[5].find("root") == 1:  # if 'root' is present in the user home directory
            print i[0]  # print the user name
                                

Run the program
---------------

We shall save the above code as "user finder.py".
To run the script, follow the steps.

1. Change the file's permissions and make it executable::

   $ chmod +x user\ finder.py

2. Execute the file::

   $ ./user\ finder.py

*Alternatively*, try::

    $ python user\ finder.py



