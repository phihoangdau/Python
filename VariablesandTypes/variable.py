# variable integer 
from email.errors import MissingHeaderBodySeparatorDefect


myint = 7
print(myint)

# variable floating
myfloat = 7.0
print(myfloat)
myfloat = float(8)
print(myfloat)

# variable String

mystring = "Hello"
print(mystring)
#\n is the special character, means newline!
mystring = "Doesn't mean.\nYou're right!!"
print(mystring)
print('C:\some\name')
# don't want use \ as a special character, we add r before the first quote
print(r'C:\some\name')


# use triple-quote to span multiple lines: """....."""
print("""\
Usage: thingy [OPTIONS]
    -h                  Display this usage message
    -H  hostname        Hostname to conect to
    """)


# String can be concatenated (glue together) with the + operator and repeated with *
# 3 times 'un', followed by 'ium'
mystring = 3 * "un" + "ium"
print(mystring)

# two or more string lterals next each other are automatically concatenated
mystring = ("Hello "
            "world !!")
print(mystring)

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)


# can be done on more than one variable "simultaneously" on the same line
a, b = 3, 4
print(a, b)


#Exercise
mystring = "hello"
myfloat = 10.0
myint = 20


# testing code
if mystring == "hello":
    print("String: %s" % mystring)
# isinstance check myfloat variable is float or not 
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint) 
# asdas