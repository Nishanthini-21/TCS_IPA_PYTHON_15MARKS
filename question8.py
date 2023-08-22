'''
Question:Valid score list; range of valid score (0<x<=100). 
If the element is valid then append ini new list
SAMPLE I/O:
----------------------------------------------------------
Input:
5
10
20
101
90
0

Output:
valid scores:[10,20,90]
'''
#solution
def valid_score(l):
    l1=[]
    for i in l:
        if 0<i<=100:
            l1.append(i)
    return l1        
            

l=[]
for i in range(int(input())):
    l.append(int(input()))
output=valid_score(l)
if len(output)==0:
    print("no valid found")
else:
    print(output)


