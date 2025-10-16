import re

text = input()
if re.search(r"^ab*$", text):
    print("True")
else:
    print("False")