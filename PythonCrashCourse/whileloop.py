# while loop and user input
# promt = "\nTell me the messages, I will repeat it to you"
# promt += "\nEnter 'quit' to exit the program: "

# message = ""
# # while message != "quit":
# #     message = input(promt)
# #     if message != "quit":
# #         print(message)
# # we can use of the variable flag to determine whether the program is stopped or not
# flag = True # we can name anything no need to be flag
# while flag:
#     message = input(promt)
#     if message == "quit":
#         flag = False
#     else:
#         print(message)

# # 7.4
# prompts = "\nTell me what are toppings you put on your pizza"
# prompts += "\nEnter 'quit' to finish your pizza: "

# flag = True
# pizza = ""
# while flag:
#     pizza = input(prompts)
#     if pizza == "quit":
#         flag = False
#     else:
#         print("Your topping " + pizza + " is added!")

# # 7.5
# age = ""
# while True:
#     age = input("\nEnter your age to see the price of the ticket: ")
#     age = int(age)

#     if age < 3:
#         print("The price is 0$")
#     elif age <= 12:
#         print("The price is 10$")
#     elif age > 12:
#         print("The price is 15%")
#     break

# loop with Lists and Dictionaries

unconfirmed_users = ["alice", "bob", "candy"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for user in confirmed_users:
    print(user.title())

# Remove all instances of specific value from a list
pets = ["dog", "cat", "goldfish", "cat", "rabbit", "cat"]
print(pets)
while "cat" in pets:
    pets.remove("cat")
print(pets)

# Filling a Dictionary with user input
# responses = {}
# polling_active = True

# while polling_active:
#     # Prompt the person's name and responnse
#     name = input("\nWhat is your name? ")
#     response = input("which mountain would you like to climb someday?")

#     # store their response in the dictionary
#     responses[name.title()] = response

#     # Find out if anyone else is going to the the poll
#     repeat = input("Would you like to let another person respond? (yes/ no) ")
#     if repeat == "no":
#         polling_active = False 

# Polling is complete. Show the result
# print("\n--- Poll Results ---")
# for name,response in responses.items():
#     print(name + " would you like to climb " + response + ".")

# 7.8 and 7.9
sandwich_orders = ["pastrami" , "chicken", "egg", "pastrami", "roast beef", "pastrami"]
finished_sandwich = []
print("\nSorry for the inconvenience, we have run out of pastrami\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich is not "pastrami":
        print("I made your " + current_sandwich.title() + " sandwich")
        finished_sandwich.append(current_sandwich)
    else:
        continue

print("\nThis the list of your sandwich that you ordered\n")
for sandwich in finished_sandwich:
    print(sandwich.title() + " sandwich")

# 7.10
dream_vacations = {}
polling_status = True
while polling_status:
    name = input("\nTell me your name: ")
    dream_vacation = input("What is your dream vacation? ")

    # save the anwsers to dream_vacation
    dream_vacations[name.title()] = dream_vacation.title()

    #repeat
    repeat = input("\nWould you like to let another person respond? (yes/no) ")
    if repeat == "no":
        polling_status = False

print("\n--- Poll Results ---")
for name,dream in dream_vacations.items():
    print(name + " would like to go to " + dream)