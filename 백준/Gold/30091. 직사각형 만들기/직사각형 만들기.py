n,*l=map(int,open(0).read().split())
c={}
for i in l:c[i]=c.get(i,0)+1
l=sorted(c)
d={}
m=0
for i in range(len(l)):
    a=l[i]
    d[a+a]=d.get(a+a,0)+c[a]//2*a*a
    m=max(m,d[a+a])
    for j in range(i+1,len(l)):
        b=l[j]
        d[a+b]=d.get(a+b,0)+a*b*min(c[a],c[b])
        m=max(m,d[a+b])
print(m)