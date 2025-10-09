def square(a,b):
    for i in range(a,b+1):
        yield i**2

a=int(input("Введи 1 цифру: "))
b=int(input("Введи 2 цифру: "))

x=square(a,b)

for i in x:
    print(i)