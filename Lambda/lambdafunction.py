# usually we using the dev keyword somewhere in the code and call it whether we need to use 
def sum(a,b):
    return a+b
x = 1
y = 2
z = sum(x,y)
print(z)

# we use lambda function instead
# you_function_name = lambda inputs : output

sum = lambda x,y : x + y
c = sum(x,y)
print(c)

def odd (a):
    if (a % 2) == 1:
        return True
    else:
        return False
l = [2,4,7,3,14,19]
for i in l:
    print(odd(i))


for r in l:
    odd1 = lambda x : (x % 2) == 1
    print(odd1(r))