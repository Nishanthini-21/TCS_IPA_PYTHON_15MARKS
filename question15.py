'''
Question: Take an integer as an input
calculate the sum of its digit if the sum%3 then print True else print False.

sample i/o:
input1  : 765
output1 : True

input1  : 877
output1 : False
'''
#solution
integer=int(input())
sum=0
for i in str(integer):
    sum+=int(i) 
if sum%3==0:
    print("True")
else:
    print("False")
