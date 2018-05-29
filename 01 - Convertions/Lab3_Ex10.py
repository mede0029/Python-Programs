# Write a program that will compute MPG for a car.
# Prompt the user to enter the number of miles driven and the number of gallons used.
# Print a nice message with the answer.

number_miles = input ("How many miles did you drive?")
number_miles = float(number_miles)

number_gallons = input ("How many gallons did you use?")
number_gallons = float(number_gallons)

MPG = number_miles / number_gallons
MPG = str(MPG)

print("Your MPG is " + MPG)
