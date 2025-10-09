def desc(n):
    for i in range(0,n+1):
        x=n-i
        yield x
            
n=int(input("Введи 1 цифру: "))

y=desc(n)

for i in y:
    print(i)
    