a=("Shadiyar","Daniyar","Didar","Damir")
b=list(a)

b.pop(1)
a=tuple(b)
print(a)

# 2

x=("Shadiyar","Daniyar","Didar","Damir")
y=("hey !",)
x+=y
print(x)

#3

z=("Shadiyar","Daniyar","Didar","Damir")
del z
## print(z)    this will be error because tuple is already deleted 