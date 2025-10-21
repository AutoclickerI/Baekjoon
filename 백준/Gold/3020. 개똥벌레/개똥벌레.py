N,H,*l=map(int,open(0).read().split())
d,t=map(sorted,(l[::2],l[1::2]))
c=0
s={}
for i in t:
    c+=1
    s[i+1]=s.get(i+1,0)-1
for i in d:
    s[H-i+1]=s.get(H-i+1,0)+1
a=0
m=1e9

for i in range(1,H+1):
    if c==m:
        a+=1
    if c<m:
        m=c
        a=1
    c+=s.get(i,0)
print(m,a)