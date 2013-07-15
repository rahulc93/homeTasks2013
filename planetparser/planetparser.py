#!/usr/bin/env python

import urllib2
from bs4 import BeautifulSoup

blog_url = "http://planet.fedoraproject.org/"
url_open = urllib2.urlopen(blog_url)
html_source = url_open.read()
soup = BeautifulSoup(html_source)
title_list = soup.find_all("div", class_="blog-entry-title")
author_list = soup.find_all("div", class_="blog-entry-author")
for i in range(len(title_list)):
    soup_title = BeautifulSoup(str(title_list[i]))
    title = soup_title.get_text()
    print "Title: ", title
    soup_author = BeautifulSoup(str(author_list[i]))
    author = soup_author.div.a.get_text()
    print "Author: ", author
    print ""

