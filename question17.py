'''
Question:Count of spaces and characters in the given string
sample i/o:
input:
Hello This is ABCD from XYZ City

Output:
spaces count: 6
character count: 26
'''
#solution
string=input()
space_count=0
char_count=0
for i in string:
    if i.isspace():
        space_count+=1
    else:
        char_count+=1
print("spaces count:",space_count)
print("character count:",char_count)
