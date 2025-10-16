import re 


text=input()

result=re.sub("[A-Z]",'_',text)
print(result)