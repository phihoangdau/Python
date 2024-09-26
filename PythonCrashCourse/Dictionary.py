# Accessing the key in the dictionary
alien_0 = {"color": "green", "points": 5}
# Get the value of color key
print(alien_0["color"])
new_point = alien_0["points"]
print("You just earned " + str(new_point) + " points!")
# Add new key-value pairs in the dictionary
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)
# modify value in a dictionary
alien_0["color"] = "yellow"
print(alien_0["color"])
alien_1 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print("Original position: " + str(alien_1["x_position"]))
if alien_1["speed"] is "slow":
    x_increment = 1
elif alien_1["speed"] is "medium":
    x_increment = 2
else:
    x_increment = 3
# the new position is the old plus increment.
alien_1["x_position"] = alien_1["x_position"] + x_increment
print("New position: " + str(alien_1["x_position"]))
# remove key-value pairs
print(alien_0)
del alien_0["x_position"]
print("After remove x_position " + str(alien_0))

# 6.1
person_information = {
    "first_name": "Phi",
    "last_name": "Hoang",
    "age": 26,
    "city": "Ho Chi Minh City"
}
for key,value in person_information.items():
    print(key + ": " +str(value))
# 6.2
favorite_number = {
    "Barney": 7,
    "Ted": 5,
    "Robin": 99,
    "Marshal": 8,
    "Lily": 1
}
for key, value in favorite_number.items():
    print("Favorite number of " + key + " is: " + str(value))
# 6.3
programming_word = {
    "print": "print the text inside the print function",
    "append": "add the element into the list",
    "if": "for the condition",
    "for": "this is the iteration",
    "del": "delete item"
}
# looping through all Key value
for key, value in programming_word.items():
    print("the " + key + " is used for: " + value)

#looping through all the keys in a dictionary. use key() method
for name in favorite_number.keys(): # -> the same with for name in favorite_number:
    print(name.title())
# only print the value when it matches condition
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
friends = ["phil", "sarah", "roger", "murphy", "zara"]
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + 
        " , I see your favorite languge is " + 
        favorite_languages[name].title() + "!")
if "ben" not in favorite_languages.keys():
    print("Ben, please take our poll!\n")
# looping through key in order, use sorted() function
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
# looping through all values in a dictionary
print("The following languages have been mentioned!")
for language in favorite_languages.values():
    print(language.title())
# this will pull all the values from dictionary without checking for repeats
# to see each language chosen without repetition, we can use set
print("this one not repeat")
for language in set(favorite_languages.values()):
    print(language.title())

# 6.5
rivers = {
    "nile": "egypt",
    "amazon": "south america",
    "ganges": "india"
}
for key,value in rivers.items():
    print("The " + key.title() + " runs through " + value.title())
print("\nThese are 3 famous rivers around the world:")
for river in rivers.keys():
    print(river.title())
print("\nThese are names of country that rivers run through:")
for city in rivers.values():
    print(city.title())

# 6.6
for key in favorite_languages.keys():
    if key in friends:
        print("Thank " + key.title() +", for taking the poll")
    else:
        print("Hello " + key.title() + ", please take our poll!")