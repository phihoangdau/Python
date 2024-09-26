# Similar to Array but works with key and value
phonebook = {}
phonebook["John"] = 123
phonebook["Jack"] = 456
phonebook["Jill"] = 789
print(phonebook)


# Alternatively 

phonebook1 = {
    "John" : 11111111,
    "Jack" : 22222222,
    "Jill" : 33333333
}
print(phonebook1)

# Dictionaries can be iterated over, does not keep the order of the values stored in it.
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# Removing a value
del phonebook1["John"]
print(phonebook1)
#or
phonebook.pop("Jill")
print(phonebook)

#Exercise: Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.
phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  
# your code goes here
phonebook.update({"Jake" : 938273443})
# or phonebook["Jake"] = 938273443
phonebook.pop("Jill")
print(phonebook)
# testing code
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")  
