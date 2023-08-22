#19 check palindrome
'''Question and sample i/o:

input:
3
malayalam
Radar
nitish

output:
malayalam
Radar
'''
#solution
def function(l):
    l1=[]
    for word in l:
        if word.lower()==word[::-1].lower():
            l1.append(word)
            
    return l1
l=[]
for i in range (int(input())):
    l.append(input())
    
output=function(l)
if len(output)==0:
    print("not palindrome found")
else:
    for i in output:
        print(i)



