'''To print smallest vowel of the string
SAMPLE I/O:
Input:
matrix
Output:
a
'''

#solution
vowels="aeiouAEIOU"
string=input()
s=[]
for i in string:
    if i in vowels:
        s.append(i)
s=sorted(s)
print(s[0])
