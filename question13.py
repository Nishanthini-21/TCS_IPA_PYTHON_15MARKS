'''
Question: To count the number of times the given word is repeated in the input strings
sample i/o:

input:
5
Hello World
hi I am hello
hello this is Hello
TCS Xplore
how are you
hello

output:
4
'''
#solution
l=[]
for i in range(int(input())):
    j=input().split()
    l+=j
target=input()
count=0
for i in l:
    if i.upper()==target.upper():
        count+=1
if count==0:
    print("no match")
else:
    print(count)
