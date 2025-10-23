## Write a Python program to delete file by specified path.
## Before deleting check for access and whether a given path exists or not.

import os
file = r"C:\Users\Админ\Documents\PP2\LABS\lab_6\Directories and Files\2-copy.txt" 

if os.path.exists(file):
    if os.access(file, os.R_OK):
        os.remove(file)  
        print("ты удалил")
    
else:
    print("Файл не существует")