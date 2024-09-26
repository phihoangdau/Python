greeting = "hello Python!!!"
print(greeting)


firstname = "ada"
lastname = "lovelace"
fullname = firstname + " " + lastname
message = "hello, " + fullname.title() + "!"
print(message)


#Stripping whitespace
#To remove whitespace in the string we use rstrip() method

favorite_languge = ' python '
# right side
favorite_languge_r = favorite_languge.rstrip()
# left side
favorite_languge_l = favorite_languge.lstrip() 
print(favorite_languge_r)
print(favorite_languge_l)