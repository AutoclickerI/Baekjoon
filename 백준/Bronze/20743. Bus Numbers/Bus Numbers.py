n=int(input())
d={}
r=[]
s=range(1,74)
for i in s:
 for j in s[i:]:t=i**3+j**3;r+=[-t]*(t in d);d[t]=1
print(([-i for i in sorted({*r})if-i<=n]+['none'])[0])