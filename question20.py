'''Question:
find max and min value of the list, then subtract the min value from max, the rotate the list from the value gained after subtraction.
input:
5
4
3
5
2
1
output:
[4, 3, 5, 2, 1]
4
[1, 4, 3, 5, 2]
'''


#solution
l=[]
for i in range(int(input())):
    l.append(int(input()))
maximum=max(l)
minimum=min(l)
difference=maximum-minimum
print(l)
print(difference)

print(l[difference:]+l[:difference])
