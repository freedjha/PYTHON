#. Write a program to print multiplication table of a given number using for loop

m =  int(input("Multiplication table:"))

for i in range(1,11):
    print(f"{m} X {i} = {m * i}")
