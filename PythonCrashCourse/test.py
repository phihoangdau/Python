def likes(names):
    if not names:
        print("no one likes this")
    elif len(names) == 1:
        print(names[0] + " likes this")
    elif len(names) == 2:
        print(str(names[0]) + " and " +str(names[1]) + " like this")
    elif len(names) == 3:
        print(str(names[0]) + ", " + str(names[1]) + " and " + str(names[2]) + " like this")
    else:
        print(str(names[0]) + ", " + str(names[1]) + " and "+ str(len(names)-2) + " others like this")
    pass
likes(["Peter", "Alex"])