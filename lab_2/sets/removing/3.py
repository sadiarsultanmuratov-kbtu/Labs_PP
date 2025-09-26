#если удаляющийся элемента не существует то в remove() выводить ошибку в терминале 

"""
a={"Hello","Hi","Hey","Good morning"}
a.remove("Hi44114")
print(a)   
"""

# но в discard() не выводить ошибку 
a={"Hello","Hi","Hey","Good morning"}
a.discard("Hi444")
print(a)