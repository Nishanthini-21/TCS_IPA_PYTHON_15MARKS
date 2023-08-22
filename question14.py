'''
Question: To print only the char present in the odd position of the string.
sample i/o:

input : Hey there!
output: e hr!
'''
#solution
string=input()
s=""
for i,v in enumerate(string):
    if (i%2)!=0:
        s+=v
print(s)
