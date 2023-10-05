def vowel(s):
    if(s=='a' or s=='e' or s=='i' or  s=='o' or  s=='u' or
       s=='A' or s=='E' or s=='I' or s=='O' or s=='U'):

        return True
    else:
        return False

s=input("Enter a character :- ")
result=vowel(s)
print(result)
