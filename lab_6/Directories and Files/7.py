## Write a Python program to copy the contents of a file to another file

first_file = r"C:\Users\Админ\Documents\PP2\LABS\lab_6\Directories and Files\2.txt"
second_file = r"C:\Users\Админ\Documents\PP2\LABS\lab_6\Directories and Files\2-copy.txt"
file = open(first_file, "r")
reading = file.read()
file.close()
file_2 = open(second_file, "w")
copying = file_2.write(reading)
file_2.close()