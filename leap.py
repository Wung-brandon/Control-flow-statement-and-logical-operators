
#program to check if a year is a leap year or not

year = int(input("Enter a year:"))
""" 
if year % 100 == 0:
    print(f'{year} is not a leap year')
elif year % 4 == 0 and year % 400 == 0:
    print(f'{year} is a leap year')
else:
    print(f'{year} is an invalid year') """
    
if year % 4 == 0:
    print(f'{year} is a leap year')
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'{year} is a leap year')
        else:
            print(f'{year} is not a leap year')   #Nested if statement
    else:
        print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')