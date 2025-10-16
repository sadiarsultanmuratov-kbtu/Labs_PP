import re

text = input()
if re.search("^[A-Z][a-z]*$", text):
    print("True")
else:
    print("False")