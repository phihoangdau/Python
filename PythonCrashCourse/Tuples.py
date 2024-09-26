# Tuples is an immuatable list, it uses parenthese instead of square brackets.
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
# does not support item assigment
# dimensions[0] = 250
# if we wanted to change our dimensions, we could redefine the entire tuple:
dimensions = (400, 100)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)
# 4.13
buffet = ("Hambugers", "Pizzas", "Chickens", "Ducks", "Beefsteaks")
print("\nOrignal Menu")
for food in buffet:
    print(food)
#buffet[0] = "Cheeses"
buffet = ("Hambugers", "Pizzas", "Chickens", "Lambs", "Ribs")
print("\nModified Menu")
for food in buffet:
    print(food)

