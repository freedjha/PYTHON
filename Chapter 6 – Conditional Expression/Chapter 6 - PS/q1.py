# Write a program to find the greatest of four numbers entered by the user

a1 = int(input ("Enter num1:"))
a2 = int(input ("Enter num2:"))
a3 = int(input ("Enter num3:"))
a4 = int(input ("Enter num4:"))

if (a1 > a2 and a1 > a3 and a1 > a4):
    print("Number 1 is the greatest of them all")

elif (a2 > a1 and a2 > a3 and a2 > a4):
    print("Number 2 is the greatest of them all")

elif (a3 > a1 and a3 > a2 and a3 > a4):
    print("Number 3 is the greatest of them all")

elif (a4 > a1 and a4 > a2 and a4 > a3):
    print("Number 4 is the greatest of them all")

elif a1 == a2 == a3 == a4:                            # (a1 = = a2 = = a3 = = a4) this will throw error
    print("All the given numbers are equal")

else:
    print("Invalid input")