'''
Question2: remove the "li" if present in each word of the string @last
------------------------------------
sample input output:
------------------------------------
input:
Richard is now happyil and satisfiesdil with his situationil

output:
Richard is now happy and satisfiesd with his situation
'''
------------------------------------
#solution
input1=input()
l=input1.split()
l1=[]
for word in l:
    if word[-2:] == "il":
        l1.append(word[0:-2])
    else:
        l1.append(word)
res=""
for i in l1:
    res=res+i+" "
print(res)
