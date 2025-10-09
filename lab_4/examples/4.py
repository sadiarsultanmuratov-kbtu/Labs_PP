class myclass:
    def __init__(self,N):
        self.N=N
    
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        if self.a<=self.N:
            x=self.a**2
            current=self.a
            self.a+=1
            return f"число: {current} квадрат: {x}"
           
            
        else:
            raise StopIteration


N=int(input())     
cl=myclass(N)

for i in cl:
    print(i)