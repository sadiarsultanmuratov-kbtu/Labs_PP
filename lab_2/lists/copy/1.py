#как можно капировать элементы с одного массива к другую ?

## This is wrong ,you copy references 

a=["Shadiyar","Temirlan","Didar","Rauan"]
b=a

#1 first way to copy copy()
c=["Shadiyar","Temirlan","Didar","Rauan"]
d=c.copy()
print(d)

#2 list()
x=["Shadiyar","Temirlan","Didar","Rauan"]
y=list(x)
print(y)

#3
z=["Shadiyar","Temirlan","Didar","Rauan"]
p=z[:]
print(p)