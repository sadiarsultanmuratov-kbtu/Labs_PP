def even(n):
    for i in range(0,n+1):
        if i%2==0:
            yield i
            
n=int(input("введи число: "))
for i in even(n):
    print(i)