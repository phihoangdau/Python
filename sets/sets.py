# set() are lists with no duplication 
print(set("my name is Eric and Eric is my name".split())) 

# also has the ability to calculate differences and intersections between other sets
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

# find the person who both on 2 sets 
print(a.intersection(b))

#find out which members attended only one of the events, use the "symmetric_difference" method:

print(a.symmetric_difference(b))

# find the list with is only in a not b and vire vesa
print(a.difference(b))
print(b.difference(a))

#pinrt all the items in two lists
print(a.union(b))