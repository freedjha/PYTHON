# #SNAKE WATER GUN
# import random

# # List of strings
# string_list = ["snake", "water", "gun"]

# # Generate a random string from the list
# computer = random.choice(string_list)

# # User input
# you = input("Enter your choice (snake, water, gun): ")

# if you = = "snake" and computer = = "water":
#     print("you win")


import random

# List of strings
string_list = ["snake", "water", "gun"]

# Generate a random string from the list
computer = random.choice(string_list)

# User input
you = input("Enter your choice (snake, water, gun): ")
print(f"computer chose:{computer}")

# Compare choices and print the result
if you == "snake" and computer == "water":
    print("You win!")
elif you == "water" and computer == "snake":
    print("You lose!")
elif you == "gun" and computer == "water":
    print("You win!")
elif you == "water" and computer == "gun":
    print("You lose!")
elif you == "snake" and computer == "gun":
    print("You lose!")
elif you == "gun" and computer == "snake":
    print("You win!")
else:
    print("It's a tie!")
