from functools import*

@cache
def maxres(s):
    r=sum(ord(i)%2 for i in s)
    if len(s)<2:
        return r
    if len(s)<3:
        return r+maxres(str(int(s[0])+int(s[1])))
    m=0
    for i in range(1,len(s)):
        for j in range(i+1,len(s)):
            m=max(m,maxres(str(int(s[:i])+int(s[i:j])+int(s[j:]))))
    return r+m

@cache
def minres(s):
    r=sum(ord(i)%2 for i in s)
    if len(s)<2:
        return r
    if len(s)<3:
        return r+minres(str(int(s[0])+int(s[1])))
    m=float('inf')
    for i in range(1,len(s)):
        for j in range(i+1,len(s)):
            m=min(m,minres(str(int(s[:i])+int(s[i:j])+int(s[j:]))))
    return r+m

s=input()
print(minres(s),maxres(s))