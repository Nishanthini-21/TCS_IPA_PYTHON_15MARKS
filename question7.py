'''
Question: To print the common element/elements present in both the lists
'''
#solution
l1=[2,2,3,4,5,6,7]
l2=[2,8,9,5,0,1]
l3=[]
for i in l1:
    if i in l2:
        l3.append(i)
l3=list(set(l3))
for i in l3:
 print(i,end=" ")
  
#output  
2 5  
