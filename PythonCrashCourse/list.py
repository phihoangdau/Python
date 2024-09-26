# #3.1
# names = ["Huy", "Bong", "Phong", "Son"]
# print(names[0]); print(names[1]); print(names[2]); print(names[-1])


# #3.2
# Greeting = "Hello, My name is"
# print(Greeting + " " + names[0].title())
# print(Greeting + " " + names[1].title())
# print(Greeting + " " + names[2].title())
# print(Greeting + " " + names[-1].title())

# #3.3
# transportations = ["Honda", "Mercedes", "Porches", "Volvo"]
# print("I would like to own a " + transportations[0])


# # Add new items to list
# # append() method add to the end of list
# transportations.append("Ducati")
# print(transportations)

# # insert elements into a list at any position
# transportations.insert(0,"Yamaha")
# print(transportations)

# # Remove items from list
# del transportations[0]
# print(transportations)

# # Using pop() method pop element at any position
# pop_trans = transportations.pop(2)
# print(transportations)
# print(pop_trans)

# # Remove item with its value, use remove() method
# transportations.remove("Volvo")
# print(transportations)



# 3.4
guest = ["Chi","Son","Khoa"]
print("Hi " + guest[0] + ", you free tonight?")
print("Hi " + guest[1] + ", you free tonight?")
print("Hi " + guest[-1] + ", you free tonight?")
# 3.5
print("Unfortunately, " + guest[-1] + " Didn't make it tonight")
guest.pop()
guest.append("Linh")
print(guest)
print("Hi " + guest[-1] + ", you free tonight?")

# 3.6
print("Hi all, I will invite more ppl to joining us for this night event")
guest.insert(0,"Tu")
guest.insert(2, "Van")
guest.append("Hiep")
print(guest)

# 3.7
# print("Due to unexpected event, tonight will be cancel. Sorry for this")
# remove_guest = guest.pop()
# print("Hi " + remove_guest + ", tonight dinner will be cancel")
# remove_guest = guest.pop()
# print("Hi " + remove_guest + ", tonight dinner will be cancel")
# remove_guest = guest.pop()
# print("Hi " + remove_guest + ", tonight dinner will be cancel")
# remove_guest = guest.pop()
# print("Hi " + remove_guest + ", tonight dinner will be cancel")
# print("Hi " + guest[0] + ", you free tonight?")
# print("Hi " + guest[1] + ", you free tonight?")
# del guest[:]
# print(guest)

# Organizing a List
# sort() method this will change the order permanently

cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)
# changes the order of the list in alphabetical 
cars.sort()
print(cars)
# we can also sort this in reverse alphabetical order by passing the argument reverse=True
cars.sort(reverse=True)
print(cars)

# sorting a list temporarily with the sorted() function. the sorted() function also accept the argument reverse=True
cars = ["bmw", "audi", "toyota", "subaru"]
print("Here is the original list:")
print(cars)
print("\nHere is the sorted version:")
print(sorted(cars))
print("Here is the original again:")
print(cars)

# print a list in reverse order not alphabetical order
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)
cars.reverse()
print(cars)

# length of a list by using len() function
cars = ["bmw", "audi", "toyota", "subaru"]
print(len(cars))


# 3.8
places = ["Japan", "Korean", "USA", "Europe", "Singapore"]
print(places)
print("Here is the alphabetical order:")
print(sorted(places))
print("\nHere is the orignal:")
print(places)
print("\nHere is the reverse alphabetical order:")
print(sorted(places, reverse=True))
print("\nHere is the orignal again:")
print(places)
print("\nHere is the reverse of that list:")
places.reverse()
print(places)
print("\nHere is the orignal again:")
places.reverse()
print(places)
print("Here is the alphabetical order again:")
places.sort()
print(places)
print("\nHere is the reverse alphabetical order again:")
places.sort(reverse=True)
print(places)
print("Here is the number of the Guest from 3.6")
print(len(guest))