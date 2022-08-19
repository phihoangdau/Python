# # A list of Dictionaries
# aliens = []
# for alien_number in range(10):
#     new_alien = {
#         "color": "green",
#         "points": "5",
#         "speed": "slow"
#     }
#     aliens.append(new_alien)
# for alien in aliens[:3]:
#     if alien["color"] == "green":
#         alien["color"] = "yellow"
#         alien["points"] = 10
#         alien["speed"] = "medium"
#     elif alien["color"] == "yellow":
#         alien["color"] = "red"
#         alien["points"] = 15
#         alien["speed"] = "fast"
# for alien in aliens[:5]:
#     print(alien)
# print("Total number of aliens: " + str(len(aliens)))

# # a list in a dictionary
# favorite_languages = {
#     "jen": ["ruby", "python"],
#     "sarah": ["c"],
#     "edward": ["ruby", "go"],
#     "phil": ["python", "haskell"]
# }
# for name, languages in favorite_languages.items():
#     print("\n" + name.title() + "'s favorite languages are:")
#     for language in languages:
#         print("\t" + language.title())
# # dictionaries in dictionary
# users = {
#     "aeinstein": {
#         "first": "albert",
#         "last": "einstein",
#         "location": "priceton"
#     },
#     "mcurie": {
#         "first": "marie",
#         "last": "curie",
#         "location": "paris"
#     }
# }
# for username, user_info in users.items():
#     print("\nUsername: " + username)
#     full_name = user_info["first"] + " " + user_info["last"]
#     location = user_info["location"]

#     print("\tFull name: " + full_name.title())
#     print("\tLocation: " + location.title())

# 6.7
phihoang = {
    "first_name": "phi",
    "last_name": "hoang",
    "age": 26,
    "city": "ho chi minh"
}
sister = {
    "first_name": "thuy",
    "last_name": "nga",
    "age": 30,
    "city": "ho chi minh"
}
hachi = {
    "first_name": "ha",
    "last_name": "chi",
    "age": 25,
    "city": "da lat"
}
people = [phihoang, sister, hachi]
for person in people:
    print(person)

# 4.8
bito = {
    "kind": "rabbit",
    "owner": "hoang"
}
wheek = {
    "kind": "guinea pig",
    "owner": "chi"
}
tino = {
    "kind": "dog",
    "owner": "chi"
}
pets = [bito, wheek, tino]
for pet in pets:
    print(pet)

# 6.9
favorite_places = {
    "hoang": ["da lat", "europe", "ha noi"],
    "chi": ["sapa", "vung tau", "europe"],
    "mom": ["hometown", "japan", "usa"]
}
for names, place_information in favorite_places.items():
    print("\nName: " + names.title())
    print("favorite places are:") 
    for place in place_information:
        print(place.title())

# 6.10
favorite_number = {
    "Barney": [7,77,777,7777],
    "Ted": [5,55,555],
    "Robin": [9,99,999],
    "Marshal": [8,88,888],
    "Lily": [1,11,111]
}
for names,numbers in favorite_number.items():
    print("\nName: " + names.title())
    print("Favorite numbers are:")

    for number in numbers:
        print(number)

# 6.11
cities = {
    "hochiminh": {
        "country": "viet nam",
        "population": 9000000,
        "fact": "Ho Chi Minh City Has a Rich Coffee Culture"
    },
    "paris": {
        "country": "france",
        "population": 2000000,
        "fact": "Paris Is Referred To As The City Of Light"
    },
    "rome": {
        "country": "italy",
        "population": 3000000,
        "fact": "More than 1.3 million euros is tossed every year in the Trevi Fountain"
    }
}
for city, information in cities.items():
    print("\nName: " + city.title())
    for info,value in information.items():
        print("\t" + info + ": "+ str(value))