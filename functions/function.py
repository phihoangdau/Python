# Functions in python are defined using the block keyword "def" and followed with the function name as the block's name
from re import X


def myfunction():
    print("Hello from my fuction!")

# Fuctions may also receive arguments (variable passed from the caller to the function):
def myfunction_with_args(username, greeting):
    print("Hello, %s , From my function!, I wish you %s" % (username, greeting))


# Fuctions may return a value to the caller, using the keyword 'return' 

def sum_two_number(a, b):
    return a + b

# call function
myfunction()

myfunction_with_args("John Doe", "a good night")

x = sum_two_number(1, 2)
print(x)


#Exercise

# Modify this function to return a list of strings as defined above
def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
