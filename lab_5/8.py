import re
text=input()
result = re.findall("[a-z]+|[A-Z][a-z]*", text)
print(result)