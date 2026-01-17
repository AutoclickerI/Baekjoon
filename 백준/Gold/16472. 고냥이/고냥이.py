N=int(input())
v=[0]*26
s=input()
l=r=m=0
while r<len(s):
    v[ord(s[r])-97]+=1
    r+=1
    while N<len([i for i in v if i]):
        v[ord(s[l])-97]-=1
        l+=1
    m=max(m,r-l)
print(m)