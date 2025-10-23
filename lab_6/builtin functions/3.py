## Write a Python program with builtin function that checks whether a passed string is palindrome or not.

def polindrom(x,y):
    for i in x:
        for j in y:
            if i!=j:
                return False
            return True
        
        
x=input("введи текст:")

y=reversed(x)

z=polindrom(x,y)
print(z)