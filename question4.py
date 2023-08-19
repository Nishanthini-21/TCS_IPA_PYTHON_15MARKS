'''
Question4: count the number of alphabets and the numbers and print the alphabets count first if it is higher than number count and viceversa

Sample input and output:
--------------------
input1:
abcd123

output1:
Alphabets:4
Numbers:3
---------------------
input2:
abc1234

output2:
Numbers:4
Alphabets:3
--------------------
input3:
abcd

output3:
Alphabets:4
--------------------
input4:
1234

output4:
Numbers:4
--------------------
'''

#solution
input1=input()
alpha_count=0
number_count=0
for i in input1:
    if i.isalpha():
        alpha_count+=1 
    elif i.isdigit():
        number_count+=1 
if number_count==0:
    print(f"Alphabets:{alpha_count}")
elif alpha_count==0:
    print(f"Numbers:{number_count}")
elif number_count>alpha_count:
    print(f"Numbers:{number_count}")
    print(f"Alphabets:{alpha_count}")
elif number_count<alpha_count:
    print(f"Alphabets:{alpha_count}")
    print(f"Numbers:{number_count}")
