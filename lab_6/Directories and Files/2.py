## Write a Python program to check for access to a specified path. Test the existence, 
## readability, writability and executability of the specified path

import os
path= r"C:\Users\Админ\Documents\PP2\LABS"
def checking(path):
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))
    
checking(path)