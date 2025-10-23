## Write a Python program to count the number of lines in a text file.


file = open(r'C:\Users\Админ\Documents\PP2\LABS\lab_6\Directories and Files\4.py')

count = 0
for line in file:
    count += 1
print(count)