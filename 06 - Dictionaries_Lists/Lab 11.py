pcode = input("Please type the 6 digits of a postal code in Canada: > ")
pcode = (pcode.upper())
s1 = pcode[:1]
s2 = pcode[1:2]

codes = dict( )
codes = {"A" : "New Foundland" ,
         "B" : "Nova Scotia" ,
         "C" : "Prince Edward Island" ,
         "E" : "New Brunswick" ,
         "G" : "Quebec" ,
         "H" : "Quebec" ,
         "I" : "Quebec" ,
         "K" : "Ontario" ,
         "L" : "Ontario" ,
         "M" : "Ontario" ,
         "N" : "Ontario" ,
         "P" : "Ontario" ,
         "R" : "Manitoba" ,
         "S" : "Saskatchewan" ,
         "T" : "Alberta" ,
         "V" : "British Colombia" ,
         "X" : "Nunavut or Northwest Territories" ,
         "Y" : "Yukon" ,
         }

if s1 not in codes:
    print("Sorry, the first character of the postal code is not correct. \nThis is not a valid postal code in Canada.")
else:
    if s2 == "0":
        print("This postal code is from a rural address in {}.".format(codes[s1]))
    else:
        print("This postal code is from an urban address in {}.".format(codes[s1]))
