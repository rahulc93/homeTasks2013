#!/usr/bin/env python

import feedparser

feed = feedparser.parse("http://planet.fedoraproject.org/rss20.xml")  # parsing the feed from the recquired URL
for x in range(len(feed.entries)):  # iterating throgh the items in the entries list
    author, title = feed.entries[x].title.split(":", 1)  # extracting the names of authors and titles from the list
    print "\nAuthor: ", author, "\nTitle: ", title  # printing the information obtained

