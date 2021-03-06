planetparser
============

In this assignment we will be printing the titles of each blog post and their respective authors' names.
We are printing them from this `site <http://planet.fedoraproject.org>`_

Source Code
-----------

The code for the problem can be found `here <https://raw.github.com/rahulc93/homeTasks2013/master/planetparser/planetparser.py>`_

Solution
--------

Here is the solution to the problem.

.. code:: python
    
    #!/usr/bin/env python
     
    import urllib2
    from bs4 import BeautifulSoup
       
    blog_url = "http://planet.fedoraproject.org/"  # the link from which to read the blog posts and authors
    url_open = urllib2.urlopen(blog_url)  # opening the URL of the blog
    html_source = url_open.read()  # reading the html source code of the blog page and storing it into 'html_source'
    soup = BeautifulSoup(html_source)  # passing "html_doc" into the BeautifulSoup constructor
    title_list = soup.find_all("div", class_="blog-entry-title")  # extracting a list of all the titles from the blog
    author_list = soup.find_all("div", class_="blog-entry-author")  # extracting a list of all the authors to the blog posts from the blog
    for i in range(len(title_list)):  # iterating through the length of title_list
        soup_title = BeautifulSoup(str(title_list[i]))  # passing the i-th element of title_list to BeautifulSoup costructor
        title = soup_title.get_text()  # storing the title of the post in 'title'
        print "Title: ", title  # printing the title of the post
        soup_author = BeautifulSoup(str(author_list[i]))  # passing the i-th element of author_list to BeautifulSoup constructor
        author = soup_author.div.a.get_text()  # storing the author's name in 'author'
        print "Author: ", author  # printing the author's name
        print ""  # printing a newline
                                                 
    
Run the program
---------------

To run this program, save the code as *planetparser.py*, and follow the steps

1. Change the file's permissions and make it executable::

   $ chmod +x planetparser.py

2. Execute the file::

   $ ./planetparser.py

*Alternatively*, you can also do::

    $ python planetparser.py


