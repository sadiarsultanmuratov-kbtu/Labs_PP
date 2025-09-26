#1

x=["moon", "sun","earth","saturn","venera","star","dust","I must delete this one"]
print("this is function of remove" )
x.remove("I must delete this one")
print(x)

#2

y=["moon", "sun","earth","saturn","I must delete this one","venera","star","dust"]
print("this is function of pop" )
y.pop(4)
print(y)

#3

z=["moon", "sun","earth","saturn","venera","star","dust","I must delete this one"]
print("this is function of pop()" )
z.pop()
print(z)

#4

a=["moon", "sun","earth","saturn","venera","star","dust","I must delete this one"]
print("this is function of clear" )
a.clear()
print(a)



#6

c=["moon", "sun","earth","saturn","venera","star","dust","I must delete this one"]
print("this is function of del[]" )
del c[7]
print(c)