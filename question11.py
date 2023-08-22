'''
Question: To find position of second occurance of a given number in a given list of numbers
INPUT:
5
3
4
3
7
4
3
OUTPUT:
2
'''
#SOLUTION
def position(l,n):
    k=2
    for i,v in enumerate(l):
        if v==n:
            k-=1
            if k==0:
                return i 
                break
    return 0
l=[]
for i in range(int(input())):
    l.append(int(input()))
n=int(input())
output=position(l,n)
if output==0:
    print("not found")
else:
    print(output)
