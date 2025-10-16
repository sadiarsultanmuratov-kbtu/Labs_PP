import re

text = input()
if re.search("^[a-z](_?[a-z])*$", text):
    print("True")
else:
    print("False")