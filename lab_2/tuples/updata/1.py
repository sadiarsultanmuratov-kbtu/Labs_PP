# мы не можем добавлять или удалять элементы в тюпл так как они не изменямы 

# но можно таким образом 

# 1

a=("Shadiyar","Daniyar","Didar","Damir")
y=list(a)

y.append("Temirlan")
a=tuple(y)
print(a)
print(type(a))

#2

b=("hi","hey","hello")
y=list(b)
y.insert(2,"this is my inserting")

b=tuple(y)
print(b)
print(type(b))

c=(100,200,300,400,580)

d=list(c)

d.remove(200)
c=tuple(d)
print(c)
