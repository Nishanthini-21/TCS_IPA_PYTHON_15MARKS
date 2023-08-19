'''
Question1: Count the number of times, the given word is repeated in the user input strings(case insensitive)
----------------------------------------------
sample input and output:
----------------------------------------------
input:
3
HELLO ANMOL
Hello friends!
good morning
hello

output:
count of given word:2
'''

#solution
def function(l,string1):
    count=0
    for v in l:
        if v.lower()==string1.lower():
            count+=1 
    
    return count


l=[]
for i in range(int(input())):
    j=input().split(" ")
    l=l+j
print(l)
str1=input()

output=function(l,str1)
if output==0:
    print("word not found in input strings")
else:
    print(f"count of given word:{output}")



