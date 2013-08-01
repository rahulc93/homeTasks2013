dup_images
==========

In this assignment, we pass some paths as command line arguments, and the script will tell us if there exists a duplicate file for a image file.

Source Code
-----------

The source code for the above problem can be found `here <https://github.com/rahulc93/homeTasks2013/tree/master/dup_images>`_

Solution
--------

The solution to the problem is shown below.

.. code:: python

    #!/usr/bin/env python

    import os
    import sys
    import fnmatch
    from PIL import Image

    def get_exif(path, image):
	if path[-1] != '/':
	    path += '/'
	img = Image.open(path+image)  # adding the file-name to the 'path' string and creating Image object
	exif_data = img._getexif()  # obtaining exif data for the 'img' object
	return exif_data  # return the data obtained

    dir_list = sys.argv[1:]  # list of directory paths given as input
    for path in dir_list:  # iterating through 'dir_list'
	if not os.path.exists(path):  # 'path' is not a valid path
	    print "Invalid path: %r" % path  # display error message
	    dir_list.remove(path)  # remove the invalid path from 'dir_list'

    jpeg_files = []  # list of all the jpeg files
    for count, path in enumerate(dir_list):  # iterating through 'dir_list'
	jpeg_files.append([path])  # adding the 'path' to 'jpeg_files' as a list
	for fl in os.listdir(path):  # iterating through the directory entries in 'path'
	    if fnmatch.fnmatch(fl, '*.JPG'):  # a jpg file has been encountered
		jpeg_files[count].append([fl])  # add the filename to 'jpeg_files'

    for entries in jpeg_files:  # scanning the 'jpeg_files' list
	if len(entries) == 1:  # no jpg files present in a particular entry
	    jpeg_files.remove(entries)  # remove the unwanted entry

    for entries in jpeg_files:  # iterate through the list entries of 'jpeg_list'
	for files in entries[1:]:  # iterate through the file names in 'entries'
	    if not get_exif(entries[0], files[0]):  # no exif data for 'files' in path 'entries[0]'
		entries.remove(files)  # remove such a file entry from 'entries'

    dup_images = []  # contains information about duplicate images of 'file1'
    count = 0  # number of files without duplicates
    for index1, list1 in enumerate(jpeg_files):  # iterating through list entries of 'jpeg_files'
	for file1 in list1[1:]:  # iterating through the members of 'list1'
	    dup_images.insert(count, [file1])  # adding the name of 'file1' to 'dup_images'
	    dup_images[count].append(list1[0])  # adding the location of 'file1' to 'dup_images'
	    for index2, list2 in enumerate(jpeg_files):  # iterating through list entries of 'jpeg_files'
		for file2 in list2[1:]:  # iterating through members of 'list2'
		    if not cmp(get_exif(list1[0], file1[0]), get_exif(list2[0], file2[0])) and jpeg_files[index1][list1.index(file1)] != jpeg_files[index2][list2.index(file2)]:
			# exif data of 'file1' and 'file2' are same, and they are not the same files
			dup_images[count].append(list2[0])  # adding the location of 'file2' to 'dup_images'
			jpeg_files[index2].remove(file2)  # remove 'file2' from 'jpeg_files[index2]'
	    jpeg_files[index1].remove(file1)  # remove 'file1' from 'jpeg_files[index1]'
	    count+=1  # increment count by 1

    for entries in dup_images:  # iterate through the members of 'dup_images'
	if len(entries) == 2:  # no duplicate images found in 'entries'
	    dup_images.remove(entries)  # remove the above entry

    if len(dup_images) == 0:  # no duplicate image found for the paths provided by the user
	print 'No duplicate images found'  # display the message
    else:  # some duplicate files are present
	print '%d files with duplicate copies found.\n' % len(dup_images)  # number of duplicate files present
	for count, entries in enumerate(dup_images):  # iterate through members of 'dup_images'
	    print 'File %d: %r' % (count+1, entries[0][0])  # print file name which has duplicate images
	    for index, location in enumerate(entries[1:]):  # iterating through locations
		print 'Location %d: %r' % (index+1, location)  # print the paths to duplicate images
	    print ""  # print a newline

Run the Code
------------

To run the code, save it as *dup_images.py*, and follow the steps.

1. Change the file's permissions and make it executable::

   $ chmod +x dup_images.py

2. Execute the script::

   $ ./dup_images.py <path-1> <path-2> ... <path-n>

*Alternatively*, you can try::

    $ python dup_images.py <path-1> <path-2> ... <path-n>

.. note::

    <path-n> represents the n-th/path/to/be/scanned


