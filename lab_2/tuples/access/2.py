thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple[:4])
print(thistuple[2:])
print(thistuple[-2:])
print(thistuple[-4:])
print(thistuple[:-2])

if "mango" in thistuple:
    print("YES HERE")
    
if "orange" not in thistuple:
        print("Yes")
else:
    print("NO")