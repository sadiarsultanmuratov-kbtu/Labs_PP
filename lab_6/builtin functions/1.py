## Write a Python program with builtin function to multiply all the numbers in a list

x=list(input("your number:").split())
z=map(int,x)
y=1
for i in z:
    y*=i
    
print(y)