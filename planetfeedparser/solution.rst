planetfeedparser
================

In this assignment, we will be reading the RSS feeds of this `site <http://planet.fedoraproject.org>`_ , parse the feed, and print the title of the blog posts and their respective authors.

Source Code
-----------

The code for the above problem can be found `here <https://github.com/rahulc93/homeTasks2013/blob/master/planetfeedparser/planetfeedparser.py>`_

Solution
--------

The solution to the problem is shown below.

.. code:: python

    #!/usr/bin/env python

    import feedparser

    feed = feedparser.parse("http://planet.fedoraproject.org/rss20.xml")  # parsing the feed from the recquired URL
    for x in range(len(feed.entries)):  # iterating throgh the items in the entries list
        author, title = feed.entries[x].title.split(":", 1)  # extracting the names of authors and titles from the list
            print "\nAuthor: ", author, "\nTitle: ", title  # printing the information obtained


Run the program
---------------

To run this script, save the file as *planetfeedparser.py*, and follow the steps.

1. Change the file's permissions and make it executable::

    $ chmod +x planetfeedparser.py

2. Execute the file::

    $ ./planetfeedparser.py

*Alternatively*, you can try::

    $ python planetfeedparser.py


