class square:
    def __init__(self,N):
        self.N=N
        
    def __iter__(self):
        self.now=1
        return self
        
    def __next__(self):
        if self.now<=self.N:
            x=self.now**2
            self.now+=1
            return x
        else:
            raise StopIteration
N=int(input("Введи число: "))
square1=square(N)

for i in square1:
    print(i)
