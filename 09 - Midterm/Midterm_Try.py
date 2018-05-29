# Write a python program mt.py that:
# •	Read the file mt2.txt
# •	Ignore the first line
# •	Save the second line and all tcp lines to a text file mt3.txt. tcp6 lines must not be saved.
# Upload the file mt.py to canvas

with open("mt2.txt", 'r') as textfile:
    f = open("mt2.txt", "r")
    next(f)
    s = f.readlines()

    with open('mt3.txt', 'w') as fout:
        for item in s:
            if "tcp" in item and "tcp6" not in item:
                fout.writelines(item)

