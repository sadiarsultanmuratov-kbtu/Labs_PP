## мы в дикт не можем делать dict1=dict2 так как копируется ссылка именно изменение в другом будет во втором 

a={
    "name":"Shadiyar",
    "age":18,
    "isadult":True,
    "color_eye":["red","blue"]
}

b=a.copy()
print(b)

c=dict(a)
print(c)