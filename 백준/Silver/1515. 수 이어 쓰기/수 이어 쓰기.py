s=input()
n=i=0
while i<len(s):
    n+=1
    for c in str(n):
        if c==s[i]:
            i+=1
        if len(s)==i:
            break
print(n)