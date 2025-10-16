a = input()
i = 0
result = ""
while i < len(a):
    if a[i].isupper():
        if i > 0: 
            result += "_"
        result += a[i].lower()
    else:
        result += a[i]
    i += 1
print(result)