# Write a program that will compute the area of a circle.
# Prompt the user to enter the radius and print a nice message back to the user with the answer

PI = 3.14159

r = input("Enter the radius measurement: ")
r = float(r)
r = r ** 2

A = PI * r
A = str(A)

print("The area of this circle is: " + A)