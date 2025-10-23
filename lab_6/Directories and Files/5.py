## Write a Python program to write a list to a file.

list = ["Shadiyar","is","doing","homework"]
file = open(r'C:\Users\Админ\Documents\PP2\LABS\lab_6\Directories and Files\1.txt','w')

for i in list:
    file.write(i+ " ")
    
file.close()