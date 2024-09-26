#List comprehension 
#newlist = [expression for item in iterable if condition == True]
if __name__ == '__main__':
    x = int(input("Enter x:"))
    y = int(input("Enter y:"))
    z = int(input("Enter z:"))
    n = int(input("Enter n:"))

print([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if (a + b + c) != n])
print(range(3))