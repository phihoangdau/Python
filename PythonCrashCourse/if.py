
cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# keyword "and" used for check whether two conditions are both true simultaneously. 
age_0 = 21
age_1 = 18
if (age_0 >= 21) and (age_1 >= 21):
    print(True)
else:
    print(False)

# keyword "or" allows to check multiple conditions as well, but it passes when either or both of individual tests pass.
# only fail when both invidiual tests fail
if (age_0 >= 21) or (age_1 >= 21):
    print(True)
else:
    print(False)

# check if it is in the list or not using keyword "in"
if 'Audi' in cars:
    print(True)
else:
    print(False)

# check if is not in the list using keyword "not in"
if 'Audi' not in cars:
    print(True)
else:
    print(False)

# 5.2
foods = ["chicken", "beef", "tofu", "vegetables", "rice"]
if "beef" in foods:
    print("Yes")
else:
    print("No")

if "duck" not in foods:
    print("Don't have that in menu")
else:
    print("Yes")

grades = range(0,11)

for grade in grades:
    if grade == 0:
        score = "F"
    elif grade > 0 and grade <= 4:
        score = "D"
    elif grade <= 6:
        score = "C"
    elif grade <= 8:
        score = "B"
    else:
        score = "A"
    print("Your final grade is: " + score + ".")

# 5.3 and 5.4
alien_colors = "red"
# version if
if alien_colors is "green":
    print("You just earned 5 points")
if alien_colors is not "green":
    print("You just earned 10 points")
# version if-else
if alien_colors is "green":
    print("You just earned 5 points")
else:
    print("You just earned 10 points")

# 5.5
if alien_colors is "green":
    print("5 points")
elif alien_colors is "yellow":
    print("10 points")
else:
    print("15 points")

# 5.6
age = int(input("Enter your age: "))
if age < 2:
    print("baby")
elif age < 4:
    print("toddler")
elif age < 13:
    print("kid")
elif age < 20:
    print("teenager")
elif age < 65:
    print("adult")
elif age > 50:
    print("elder")

# 5.7
favorite_fruits = ["watermelons", "grapes", "apples"]
if "watermelons" in favorite_fruits:
    print("I love watermelons")
if "grapes" in favorite_fruits:
    print("I love grapes")
if "apples" in favorite_fruits:
    print("I love apples")
if "bananas" in favorite_fruits:
    print("I love bananas")
if "oranges" in favorite_fruits:
    print("I love oranges")

# 5.8 and 5.9
usernames = ["admin", "henry", "barney", "lion", "andrew"]
usernames = []
# check if list is empty or not
if not usernames:
    print("We have to add some users!")
else:
    for username in usernames:
        if username is "admin":
            print("Hello " + username.title() + ", would you like to see a status report?")
        else:
            print("Hello " + username.title() + ", thanh you for logging in again.")

# 5.10
current_users = ["Rachel", "Ross", "Richard", "Joey", "Phoebe"]
new_users = ["Chandler", "ROSS", "Joey", "Monica", "Ben"]
for new_user in new_users:
    if new_user.title() in current_users:
        print("The username is used,please try with the new username")
    else:
        print("The username is available")

# 5.11
ordinal_numbers = range(1,10)
for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print("1st")
    elif ordinal_number == 2:
        print("2nd")
    elif ordinal_number == 3:
        print("3rd")
    else:
        print(str(ordinal_number) + "th")