import re

text = input()
if re.search(r"^ab{2,3}$", text):
    print("True")
else:
    print("False")