## The two text files 2000_BoysNames.txt and 2000_GirlsNames.txt list the popularity of boys names and girls names in 2000.
## The format of the file is simple, one line per entry with the name followed by a space followed by the number of children
## carrying that name. You must write a python program that reads each text file then converts it into a csv format: "name",count
## then saves the entry in a csv file. The output csv file must include the following header as its first line:
## "First Name","Count"

import csv

texto=open("boys.txt", "r")
excel=open("boys.csv", "w")

excel.write("Coluna 1, Coluna 2\n")

for line in texto:
    l=line.split(' ')
    excel.write(l[0]+","+l[1])

texto.close()
excel.close()


