print("Welcome to the python pizza Deliveries")

small_pizza = 15
medium_pizza = 20
large_pizza = 25
total = 0

pepperoni_small_pizza = 2
pepperoni_medium_pizza = 3
pepperoni_large_pizza = 3

extra_cheese_pizza = 1

size = input("What is the size of do you want? 's','m' or 'l':").lower()
add_pepperoni = input("Do you want pepperoni? 'y' or 'n':").lower()
extra_cheese = input("Do you want extra cheese? 'y' or 'n':").lower()
if size == 's':
    if add_pepperoni == 'y':
        if extra_cheese == 'y':
            total = pepperoni_small_pizza + small_pizza + extra_cheese_pizza
            print(f"Your total bill is {total}$")
        elif extra_cheese == 'n':
            total = pepperoni_small_pizza + small_pizza
            print(f"Your total bill is {total}$")
    elif add_pepperoni == 'n':
        total = small_pizza
        print(f"Your total bill is {total}$")
    
elif size == 'm':
    if add_pepperoni == 'y':
        if extra_cheese == 'y':
            total = pepperoni_medium_pizza + medium_pizza + extra_cheese_pizza
            print(f"Your total bill is {total}$")
        elif extra_cheese == 'n':
            total = pepperoni_medium_pizza + medium_pizza
            print(f"Your total bill is {total}$")
    elif add_pepperoni == 'n':
        total = medium_pizza
        print(f"Your total bill is {total}$")
   
elif size == 'l':
    if add_pepperoni == 'y':
        if extra_cheese == 'y':
            total = pepperoni_large_pizza + large_pizza + extra_cheese_pizza
            print(f"Your total bill is {total}$")
        elif extra_cheese == 'n':
            total = pepperoni_large_pizza + large_pizza
            print(f"Your total bill is {total}$")
    elif add_pepperoni == 'n':
        total = large_pizza
        print(f"Your total bill is {total}$")
    
    