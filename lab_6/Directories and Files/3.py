## Write a Python program to test whether a given path exists or not.
## If the path exist find the filename and directory portion of the given path.

import os
path= r"C:\Users\Админ\Documents\PP2\LABS"

def checker(path):
    if os.path.exists(path):
        print("Name of file:", os.path.basename(path))
        print("name of directory:", os.path.dirname(path))
        return "success"

print(checker(path))

