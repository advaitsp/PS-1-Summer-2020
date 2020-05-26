# Write operations
# Open a file
fo = open("foo.txt", "wb")
fo.write( "I like prgromming in python language.\nIt's easy to learn\n")

# Close opend file
fo.close()

# Read operations
# fileObject.read([count])
# here the count represents the number of bytes to be read.
# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10);
print "Read String is : ", str
# Close opend file
fo.close()

# File positions
# fo.tell()
# gives the position of the cursor in the file
# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10)
print "Read String is : ", str

# Check current position
position = fo.tell()
print "Current file position : ", position

# Reposition pointer at the beginning once again
position = fo.seek(0, 0);
str = fo.read(10)
print "Again read String is : ", str
# Close opend file
fo.close()

# Renaming files
# os.rename(current_file_name, new_file_name)
import os

# Rename a file from test1.txt to test2.txt
os.rename( "test1.txt", "test2.txt" )

# Removing files
import os

# Delete file test2.txt
os.remove("text2.txt")