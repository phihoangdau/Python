# # to paste multiple of string in promt 
# promt = "If you tell us who you are, we can personalize the messages to you."
# promt += "\nWhat is your name? "
# name = input(promt)
# print("\nHello " + name + "!")

# # when you use input() function everything the users enter will store as a string
# # to accept numerical input we use int()
# height = input("How tall are your, in cm? ")
# height = int(height)

# if height >= 100:
#     print("\nYou are tall enough to ride")
# else:
#     print("\nYou will be able to ride when you're a little older.")
# # odd or even
# number = input("\nEnter a number, I will tell you if it's even or odd: ")
# number = int(number)

# if number % 2 == 0:
#     print("\nThe number " + str(number) + " is even.")
# else:
#     print("\nThe number " + str(number) + " is odd.")

# 7.1
car = input("What type of car do you want to rent? ")
print("Let me see if i can get you a " + car.upper())

# 7.1
seats = input("\nHow many people are in the dinner: ")
seats = int(seats)

if seats > 8:
    print("\nSorry, You have to wait for 15 mins to have a table ready")
else:
    print("\nTable is ready")

# 7.2
number = input("Enter a number: ")
number = int(number)

if number % 10 == 0:
    print("The number " + str(number) + " is multiple of ten")
else:
    print("The number " + str(number) + " is not multiple of ten")