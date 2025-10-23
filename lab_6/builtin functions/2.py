## Write a Python program with builtin function that accepts a string and 
## calculate the number of upper case letters and lower case letters

text = input("Введи слово: ")

uppercase=0
lowercase=0

for i in text:
    if i.isupper():
        uppercase += 1
    elif i.islower():
        lowercase += 1

print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)





