# Write a python program mt.py that:
# •	Read the file mt2.txt
# •	Ignore the first line
# •	Save the second line and all tcp lines to a text file mt3.txt. tcp6 lines must not be saved.
# Upload the file mt.py to canvas

import os
check = True

while check:
    folder = input("Inform the full path to the file you want to read:\n")
    if os.path.isfile(folder):
        check = False
    else:
        print("File does not exist.. Please inform a valid path")

tcp = []

with open(folder) as f:
    next(f)
    tcp.append(next(f))
    for line in f:
        if "tcp" in line and "tcp6" not in line:
            tcp.append(line)

    with open("mt3.txt", 'w') as df:
        for line in tcp:
            df.write(line)

print("Bye!")
