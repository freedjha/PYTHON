# Write a program to accept marks of 6 students and display them in a sorted manner

StudentMarks = []

# Getting input from the user and appending it to the list
s1 = input("Enter marks: ")
StudentMarks.append(int(s1))

s2 = input("Enter marks: ")
StudentMarks.append(int(s2))

s3 = input("Enter marks: ")
StudentMarks.append(int(s3))

s4 = input("Enter marks: ")
StudentMarks.append(int(s4))

s5 = input("Enter marks: ")
StudentMarks.append(int(s5))

s6 = input("Enter marks: ")
StudentMarks.append(int(s6))

# Printing the list before sorting
print("Marks before sorting:", StudentMarks)

# Sorting and printing the list
StudentMarks.sort()
print("Marks after sorting:", StudentMarks)

# The need to append arises because you want to collect all the input marks into a single list (StudentMarks). Without appending, the list remains empty, and thus sorting an empty list would have no effect. Appending ensures that each input mark is added to the list, allowing you to store, process, and manipulate all the marks together.