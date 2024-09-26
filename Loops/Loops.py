#For loops
from itertools import count


primes = [3,5,7]
for prime in primes:
    print(prime)


#range function
for x in range(5):
    print(x)
for x in range(3, 6):
    print(x)
for x in range(3, 8, 2):
    print(x)


#while loops
count = 0
while count < 5:
    print(count)
    count+= 1

#Break and continue 
# Prints out 0,1,2,3,4
print("Break and continue")
Count = 0
while True:
    print(Count)
    Count+= 1
    if Count >= 5:
        break

print("Prints out only odd numbers - 1,3,5,7,9")
# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 ==0:
        continue
    print(x)

#Print all but execept Swift and C++
print("Print all but execept Swift and C++") 
languages = ["Python","Java","Swift","C","C++"]
for i in languages:
    if i == "Swift":
        continue
    elif i == "C++":
        continue
    print(i)


# Prints out 0,1,2,3,4 and then it prints "count value reached 5"
i = 0
for i in range(5):
    print(i)
    i+= 1
else:
    print("count value reached %d" % i)
# Prints out 1,2,3,4
for i in range(1,10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")



#Exercise
#Loop through and print out all even numbers from the numbers list in the same order they are received
#Don't print any numbers that come after 237 in the sequence.
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
for number in numbers:
    if number == 237:
        break
    if number % 2 == 1:
        continue
    print(number)
