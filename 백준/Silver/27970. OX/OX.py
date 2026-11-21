m=10**9+7
a=0
s=input()
for i in range(len(s)):
    if s[i]=='O':
        a+=pow(2,i,m)
        a%=m
print(a)