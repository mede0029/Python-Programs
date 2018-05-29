# Write a function calcAlphaGrade that receives one parameter, a float value.
# The function returns the alphabetical grade corresponding to the numeric grade.
# The conversion map table can be found in the course outline. Note that the function does not do any error checking.
# Write a function calcNumGrade that receive six arguments, all float value. In order these arguments are numeric
# ponderation of assignments, mid term and final, then mark obtained by a student for assignments, mid term and final. The function calculates and returns the numeric grade of the student. The marking scheme can be found in the course outline. Note that the function does not do any error checking and assume that all parameters are float values.
#
# Write a program lab5.py that:
# - displays some basic instructions to the user,
# - prompts the user for the ponderation of assignments, mid term and final,
# - prompts the user for the student mark for assignments, mid term and final,
# - calculates the numerical grade,
# - calculates the alphatical grade,
# - displays on the sense hat the alphabetical grade along with a message "Congratulations, you passed"
#  if the numerical grade is greater than 50.

grade = 0

def calcNumGrade(a,b,c,d,e,f):       
    grade = (a * b) + (c * d) + (e * f)
    return grade

def calcAlphaGrade(x):
    if grade >= 90:
        x = "A+"
    elif grade <= 89 and x >= 85:
        x = "A"
    elif grade <= 84 and x >= 80:
        x = "A-"
    elif x <= 79 and x >= 77:
        x = "B+"
    elif grade <= 76 and x >= 73:
        x = "B"
    elif grade <= 72 and x >= 70:
        x = "B-"
    elif grade <= 69 and x >= 67:
        x = "C+"
    elif grade <= 66 and x >= 63:
        x = "C"
    elif grade <= 62 and x >= 60:
        x = "C-"
    elif grade <= 59 and x >= 57:
        x = "D+"
    elif grade <= 56 and x >= 53:
        x = "D"
    elif grade <= 52 and x >= 50:
        x = "D-"
    else:
        x = "F"
    return x
   
print ("This program will help you check your course progress during the semester. ")
a = float(input("What's the mark for your assignments? > "))
b = float(input("What's the weight of these assignments? Please type 0.## - percentage format > "))
c = float(input("What's the mark for your midterm? > "))
d = float(input("What's the weight of the midterm? Please type 0.## - percentage format > "))
e = float(input("What's the mark for your final term? > "))
f = float(input("What's the weight of the final grade? Please type 0.## - percentage format > "))

x = calcNumGrade(a,b,c,d,e,f)
print (x)

y = calcAlphaGrade(x)
print (y)

# In case you have sense-hat:
# import sense_hat
# s = sense_hat.SenseHat()
# s.show_message ("Your final grade is " + str(y))
#
# if x >= 50:
#     s.show_message ("Congratulations, you passed!")
