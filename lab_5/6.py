import re 

text=input()
result=re.sub("[., ]",':',text)
print(result)