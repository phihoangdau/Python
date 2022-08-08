#4.1
from cmath import pi


pizzas = ['cheese', 'beef', 'ham']
for pizza in pizzas:
    print('I like ' + pizza + ' pizza')
print('I really love pizzas!')

#4.2
animals = ['dog', 'cat', 'rabbit']
for animal in animals:
    print('A ' + animal + ' would make a great pet')
print('Any of these animals would make a great pet!')

# Making numerical Lists
# Use the range() function
for value in range(1,5):
    print(value)
numbers = list(range(1,5))
print(numbers)
# print the even number using range() function
even_numbers = list(range(2,11,2))
print(even_numbers)
print(min(even_numbers)); print(max(even_numbers))
# List comprehensions
# normal for loop
# squares = []
# for value in range(1,11):
#     squares.append(value**2)
# print(squares)
# with list comprehensions
squares = [value1**2 for value1 in range(1,11)]
print(squares)

#4.3
# for number in range(1,21):
#     print(number)
number = [number1 for number1 in range(1,21)]
print(number)

#4.4
number = [number2 for number2 in range(1,1000001)]
#print(number)

#4.5
print("Min number: " + str(min(number)))
print("Max number: " + str(max(number)))
print(sum(number))

#4.6 Odd number
Odd_numbers = [odd_number for odd_number in range(1,21,2)]
print(Odd_numbers)

#4.7 multiples of 3
Multipler_numbers = [mul_number*3 for mul_number in range(3,31)]
print(Multipler_numbers)

#4.8 and 4.9 cubes
cube_numbers = [cube_number**3 for cube_number in range(1,11)]
print(cube_numbers)


# Slicing a list
print(Odd_numbers[0:3])
#Last three elements in the list
print(Odd_numbers[-3:])


# 4.10
print("The first three items in the list are:"+ str(Odd_numbers[:3]))
print("Three items in the middle list are:"+ str(Odd_numbers[4:-3]))
print("Three items in the last list are:"+ str(Odd_numbers[-3:]))

# 4.11
friend_pizza = pizzas[:]
pizzas.append("peperoni")
friend_pizza.append("hawai")
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend favorite pizzas are:")
print([pizza for pizza in friend_pizza])