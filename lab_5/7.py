import re

text = input()

def to_camel(x):
    return x.group(1).upper()

camel_case = re.sub("_([a-z A-Z])", to_camel, text)
print(camel_case)