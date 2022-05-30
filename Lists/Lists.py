mylist = []
#append add to the list 
mylist.append(1)
mylist.append(2)
mylist.append(3)
# the first object in list is counted as 0 
print(mylist[0])
print(mylist[1])
print(mylist[2])


#prints out 1, 2, 3
for x in mylist:
    print(x)



#Exercise 

#Variables
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings = []
strings.append("hello")
strings.append("world")
names = ["John", "Erica", "Jessica"]

#Run
second_name = names[-2]

print(numbers)
print(strings)
print("The second name on the names list is %s" %second_name)