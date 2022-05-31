# Task
# The provided code stub reads and integer,n, from STDIN. For all non-negative integers i < n, print i^2.
if __name__ == '__main__':
    n = int(input("Enter number:"))
    i = 0
    while(i < n):
        if i < 0:
            continue
        else:
            print(i*i)
        i+=1

        

