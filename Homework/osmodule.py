import os

# get current working directory     
print(os.getcwd())

# change the current working directory 
os.chdir("//mnt//d//AWS//Key")
print(os.getcwd())

# create a directory name test
os.mkdir("//mnt//c//Users//1CS_LAPTOP1//OneDrive - 1CLOUDSTAR//python//python//Homework//test")

# delete a directory 
os.rmdir("//mnt//c//Users//1CS_LAPTOP1//OneDrive - 1CLOUDSTAR//python//python//Homework//test")

# delete a file
os.remove("//mnt//c//Users//1CS_LAPTOP1//OneDrive - 1CLOUDSTAR//python//python//Homework//test.py")