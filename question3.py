'''
Question3: To remove the vowels in the given string and also print the count of digits present in the string
--------------------------------
sample input and output:
--------------------------------
input:
hello wordaeiou 123

output:
hll wrd 123 and count of digit is 3
--------------------------------
'''

#solution
input1=input()
digit_count=0
l=[]
for i in input1:
    if i.isdigit():
        digit_count+=1
    if i in "aeiou":
        pass
    else:
        l.append(i)

s=""
for i in l:
    s+=i
print(f"{s} and count of digit is {digit_count}")
