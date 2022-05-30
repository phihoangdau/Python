# Python uses boolean logic to evaluate conditions
x = 2
print(x == 2) # prints out  true
print(x == 3) # prints out false
print(x < 3)  # prints out true


# the "and" and "or" boolean operators allow building complex boolean expressions
name = "Rick"
age = 23
if name == "John" and age == 23:
    print("Your name is John and you are 23 years old.")
else:
    print("You are %s and you are %s years old." % (name, age))

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")


# the "in" operator could be used to check if a specific object exists within an iterable object container such as a list:
name = "John"
if name in ["John", "Rick"]:
    print("You have passed the exam")
else:
    print("You have failed the exam")

#Testing
statement = False
another_statement = True
if statement is True:
    print("Congrats!")
    pass
elif another_statement is True:
    print("Your statement is True")
    pass
else:
    print("False")
    pass

# The "is" operator
x = [1, 2, 3]
y = [1, 2, 3]
x1 = 1
y1 = 1
print(x == y)
# x and y are lists. they are equal but not identical. because the interpreter locates them separately in memory although they are equal
print(x is y)
print(x1 is y1)

# Using "not" before a boolean expression inverts it
print(not False) # Prints out True
print((not False) == (False)) # Prints out False




#Exercise
# change this code
number = 20
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")