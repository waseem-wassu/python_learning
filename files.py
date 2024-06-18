# A file is data stored in a storage device

# types of files

# There are two types of files 
# 1. Text files (.txt etc)
# 2.Binary files(.jpg etc) 

# Python has a lot of functions for reading,updating and deleting files

# 1. opening a file :
'''
Pyhton has an open() function for opening files.
It takes 2 parameters: filename and mode

example:
open("this.txt","r")

open - built in function 
this.txt - filename
r - mode of opening
'''

# f = open("sample.txt",'r')
# data = f.read()
# print(data)
# f.close()

# f.readline() -> Reads one line from the file

# f = open("sample.txt",'r')
# data = f.readline()
# print(data)
# data = f.readline()
# print(data)
# f.close()

# Modes of opening a File
'''
r -> open for reading
w -> open for writing
a -> open for appending
t -> open for updating
'''

'''
'rb' will open for read in binary mode 
'rt' will open for read in text mode
'''

# Writing files in python
'''
In order to write to a file, we first  open it in write or append mode after which, 
we use the python's f.write() method to write to the file
'''

# To write the file
# f = open('latest.txt','w')
# f.write("heyya11")
# f.close()

# To append the new text

# f= open('tt.txt','a')
# f.write('I am appending ')
# f.close()

# with statement

# The bet way to open and close the file automatically is the with statement

# syntax
# with open("tt.txt") as f:
#     f.read()

'''
Dont need to write f.close() 
as it is done automatically
'''

# with open("tt.txt") as f:
#    rtm= f.read()
#    print(rtm)


import os

oldname = 'sample.txt'
newname = "renamed.txt"
with open(oldname) as f:
   content= f.read()

with open(newname,"w") as f:
   f.write(content)
# os.remove(oldname)

'''
f = open("sample.txt")
rtm= f.read()
if 'Waseem' in rtm:
      print("yes it is")
else :
      print("No its not available")
f.close()
 '''



