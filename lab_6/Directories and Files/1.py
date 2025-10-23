## Write a Python program to list only directories, files and all directories, files in a specified path.

import os

path= r"C:\Users\Админ\Documents\PP2\LABS"

import os

all_items = []
folders = []
files = []

for name in os.listdir(path):
    
    all_items.append(name)
    
    
    if os.path.isdir(os.path.join(path, name)):
        folders.append(name)
    

    elif os.path.isfile(os.path.join(path, name)):
        files.append(name)



print("All:", all_items)
print("Folders:", folders)
print("Files:", files)
