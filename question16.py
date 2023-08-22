'''
Question print the count of vowels and consonant present in the string
sample i/o:
----------------------------------------------------------------------
input: 
Hello World!

Output: 
vowels count: 3
consonants count: 7
'''

#solution
string=input()
vowel_count=0
consonant_count=0
for i in string:
    if i.isalpha():
        if i in "aeiouAEIOU":
            vowel_count+=1
        else:
            consonant_count+=1
print("vowels count:",vowel_count)
print("consonants count:",consonant_count)


