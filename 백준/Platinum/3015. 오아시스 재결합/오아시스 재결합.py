from bisect import*
b=bisect
r,*s=0,
for j in[*open(0)][1:]:n=-int(j);r+=len(s)-max(b(s,n-1)-1,0);s[b(s,n):]=n,
print(r)