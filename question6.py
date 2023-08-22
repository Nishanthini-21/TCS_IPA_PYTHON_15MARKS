'''
Question: The maximum repeated word in the string
Sample I/O:
-------------------------------------------------
INPUT : hello hi hello world hello
OUTPUT: hello
[hint:use dictionary]
'''


sample=input()
l=sample.split()
dicti={}

for i in l:
    if i in dicti:
        dicti[i]+=1 
    else:
        dicti[i]=1 
print(dicti)

l1=[]
for i in dicti:
    l1.append(dicti[i])
m=max(l1)
for i in dicti:
    if dicti[i]==m:
        print(i)
        break

