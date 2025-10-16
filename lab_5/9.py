import re
a = input()
result = re.sub(r'([a-z])([A-Z])', r'\1 \2', a)

print(result)