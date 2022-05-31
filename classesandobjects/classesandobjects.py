# Objecs get their variables and functions from classes. classes are essentially a template to create your objects

# basic class
from ast import Num


class Myclass:
    variable = "blah"

    def function(self):
        print("this is a message inside the class.")

# assign the above class(template) to an object:
myobjectx = Myclass()

# accessing the variable inside of the newly created object and print it out
print(myobjectx.variable)

# we can create multiple different objects in the same class
myobjecty = Myclass()
myobjecty.variable = "jackity"
print(myobjecty.variable)

# access function in the class
myobjectx.function()

# The _init()_ function is a special function that is called when the class is being initiated.It's used for assining values in a class.
class NumberHolder:

    def __init__(self, number):
        self.number = number

    def returnNumber(self):
        return self.number

var = NumberHolder(8)
print(var.returnNumber())


#Exercise 
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000

car2 = Vehicle()
car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000
# test code
print(car1.description())
print(car2.description())