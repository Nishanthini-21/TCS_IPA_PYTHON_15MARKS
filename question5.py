'''
Question5: Primenumber_count
-----------------------------
sample input and output:
-----------------------------
input:
4
3
5
7
11

output:
4
-----------------------------
'''
#solution
from sympy import *
l=[]
count=0
for i in range(int(input())):
    l.append(int(input()))
for i in l:
    if isprime(i):
        count+=1 
    else:
        pass
print(count)






