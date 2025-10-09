def square_gen(N):
    for i in range(1,N+1):
        
        yield i**2
        
N=int(input("введи число: "))
for i in square_gen(N):
    print(i)