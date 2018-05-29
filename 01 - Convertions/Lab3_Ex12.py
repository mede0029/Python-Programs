# Write a program that will convert degrees fahrenheit to degrees celsius.
#C = (F - 32) * 0.5556

F = input("What's the temperature in Fahrenheit?")
F = float(F)

C = F - 32
C = C * 0.5556
C = str(C)

print("The temperature in Celcius is " + C)



