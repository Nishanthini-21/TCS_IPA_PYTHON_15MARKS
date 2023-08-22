'''
Sample I/O:
Input:
Hyper123Lower100
output:
['HyperLower',12345100]
'''
#solution
string=input()
l=[]
al=""
nu=""
for i in string:
    if i.isalpha():
        al+=i
    elif i.isdigit():
        nu+=i 

if len(al)==0:
    l.append(int(nu))
elif len(nu)==0:
    l.append(al)
else:
    l.append(al)
    l.append(int(nu))
print(l)
