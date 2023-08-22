'''
Question:Valid and invalid string
If contains alphabets and spaces then the string is valid
if contains special character and numbers then the string is invalid
Sample I/O:

Input:
4
Nisha123
Dil@gnm  mail.com
Apple
brownie

Output:
valid count 2
invalid ciunt 2
'''
#solution
def valid(string):
    return all(ch.isalpha() or ch.isspace() for ch in string)


l=[]
for i in range(int(input())):
    l.append(input())

count=0
count1=0
for i in l:
    res=valid(i)
    if res==True:
        count+=1 
    else:
        count1+=1
print("valid count",count)
print("invalid ciunt",count1)


