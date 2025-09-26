#1

a=["hello", "Hi","Hey"]
b="Привет"
a.extend(b)

print(a)

#2

x=["hello", "Hi","Hey"]
y=(1,2,3,4,5,6)
x.extend(y)
print(x)


#3

c=["hello", "Hi","Hey"]
d={1,2,3,4,5,6}
c.extend(d)
print(c)


#4   Error syntax !!!
'''
j={1,2,3,4,5,6}
k=["hello", "Hi","Hey"]
j.extend(k)
print(j)

'''