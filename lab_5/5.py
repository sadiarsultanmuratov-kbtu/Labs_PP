import re

text = input()
if re.search("^a.*b$", text):
    print("True")
else:
    print("False")