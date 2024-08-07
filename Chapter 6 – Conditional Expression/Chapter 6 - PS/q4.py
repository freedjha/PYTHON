#Write a program to find whether a given username contains less than 10 characters or not

u = input("Username:")

if ((len(u)) >= 10):
    print("more than 10 characters in username")
    
elif ((len(u)) < 10):
    print("less than 10 characters in username")
