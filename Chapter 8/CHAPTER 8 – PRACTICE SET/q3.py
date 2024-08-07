#Write a recursive function to calculate the sum of first n natural numbers

#The sum of the first n natural numbers = n * (n+1)/2

def sum():
    n = float(input(" Enter number"))
    sum = n * (n+1)/2
    print(f"sum of numbers upto {n} = {sum}")

sum()