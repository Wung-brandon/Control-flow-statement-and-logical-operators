print("Welcome to Treasure Island")
print("Your Mission is to find the Treasure")

go = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right'\n").lower()
if go == 'left':
    island = input("You have come to a lake.There is an island in the middle of the lake.Type 'wait' to wait for a boat or type 'swim' to swim accross\n").lower()
    if island == 'wait':
        color = input("You arrived at the island unharmed.There is a house with 3 doors, one 'red', one 'yellow', and one 'blue'. Which Color do you choose?\n").lower()
        if color == 'yellow':
            print("You found a treasure. You Win!")
        elif color == 'blue':
            print("You Have entered a room of beast. Game over!")
        elif color == 'red':
            print("It's a room full of fire. Game over!")
        else:
            print("Invalid choice") 
    else:
        print("You got attacked by an angry trout. Game over!")
else:
    print("You fell into a hole. Game over!")