'''
Question:
To find the index position of the given string in the set of strings
sample i/o:
input:
4
hello good morning
abcd123fghy
Progotic.c
India
India

output:
3
'''
#solution
l=[]
for i in range(int(input())):
    l.append(input())
string=input()
for i,v in enumerate(l):
    if string.lower()==v.lower():
        print(i)
        break 
else:
    print("not found")
