# this print out "Hello, John!"
name = "John"
age = 23
print("Hello, %s" % name)
print("%s is %d years old" % (name, age))

# Any object which is not a string can be formatted using the %s operator as well
mylist = [1, 2, 3]
print("A list: %s" % mylist)

#You will need to write a format string which prints out the data using the following syntax: Hello John Doe. Your current balance is $53.44.
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)