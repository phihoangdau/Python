# the len will print out the length of the object
astring = "Hello World!"
print("single quotes are ' '")
print(len(astring))

#the first letter o in "Hello" will at index 4 
print(astring.index("o"))

#count letter l
print(astring.count("l"))

#slicing
print(astring[3:7])

#skipping one character using the third : [start:stop:step]
print(astring[3:7:2])

#reverse the string, we omit the start and stop and put the step = -1 -> means repeatedly step from right to left by 1 character 
print(astring[::-1])

#uper and lower case string
print(astring.upper())
print(astring.lower())

#determine whether the string starts with or ends with something, respectively. -> Return Boolen
print(astring.startswith("Hello"))
print(astring.endswith("asdsad"))

#split
print(astring.split(" "))



#Exercise
s = "Strings are awesome!"
# Length should be 20
print(s)
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
# Start to 5
print("The first five characters are '%s'" % s[:5])
# 5 to 10
print("the next five characters are '%s'" % s[5:10])
# Just number 12
print("the thirteenth character is '%s'" % s[12])
#(0-based indexing)
print("The characters with odd index are '%s'" %s[1::2])
# 5th-from-last to end
print("the last five characters are '%s'" % s[-5:])

# Convert everything to uppercase
print("string in uppercase: %s" % s.upper())
# Convert everything to lowercase
print("string in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str' . Good!")
# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!' . Good!")


# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))