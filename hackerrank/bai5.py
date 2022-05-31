# The year can be evenly divided by 4;

# If the year can be evenly divided by 100, then it is not a leap year

# The year is also evenly divisible by 400 then it is a leap year.
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        if year % 100 != 0:
            leap = True
        elif year % 400 == 0:
            leap = True
    return leap

year = int(input("Enter the year:"))
print(is_leap(year))
