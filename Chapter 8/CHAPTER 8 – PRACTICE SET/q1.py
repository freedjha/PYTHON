#Write a program using functions to find greatest of three numbers.

def greatest():
    # Getting input from the user
    a = int(input("Number 1: "))
    b = int(input("Number 2: "))
    c = int(input("Number 3: "))

    # Finding the greatest number
    greatest_num = max(a, b, c)
    
    # Checking for equality and printing the result
    if a == b == c:
        print("All numbers are equal")
    else:
        print(f"The greatest number is {greatest_num}")

# Calling the function
greatest()
