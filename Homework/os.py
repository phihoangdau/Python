import os
import sys
import re
# like pwd in linux get the current directory 
print(os.getcwd())
# check if file is exist or not
path1 = os.access("os.py", os.F_OK)
print("File is exist:", path1)
#checking access with os.R_OK
path2 = os.access("os.py", os.R_OK)
print("Can read:", path2)
#checking access with os.W_OK
print("Can write:", os.access("os.py", os.W_OK))
#checking access with os.X_OK
print("Can Execute:",os.access("os.py", os.X_OK))

#File path to be opened 
path = "/mnt/c/Users/1CS_LAPTOP1/OneDrive - 1CLOUDSTAR/python/python/Homework/error.log"

# this work in similar way as it works for chmod()
mode = 0o666

# contants are options for flags and can be combined using bitwise OR operator | 
# os.O_RDWR (Read and Write) | os.O_CREAT(create a file if does not exist)
flags = os.O_RDWR | os.O_CREAT

# the os.open() method returns the file description for the newly opened file
fd = os.open(path, flags, mode)
# read the file from beginning 
# os.lseek(fd, pos, how) -> fd is the file description
# pos is the position in the file with respect to given parameter how: 0(os.SEEK_SET) begin of the file, 1(os.SEEK_CUR) current position, 2(os.SEEK_END) end of the file
os.lseek(fd, 0, 0)
str = (os.read(fd, os.path.getsize(fd))).decode()
err = re.findall("")


#Close opened file
os.close(fd)