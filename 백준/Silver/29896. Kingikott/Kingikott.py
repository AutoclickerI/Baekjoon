d={}
N=int(input())
for a in[0]*N:
    s=input()
    d[s]=int(input())
c={}
for _ in[0]*int(input()):
    s=input()
    c[s]=c.get(s,0)+1
    a+=d[s]
l=[*d]
m=a
for i in range(len(d)):
    for j in range(i+1,len(d)):
        m=min(m,a-d[l[i]]*c.get(l[i],0)-d[l[j]]*c.get(l[j],0)+d[l[j]]*c.get(l[i],0)+d[l[i]]*c.get(l[j],0))
print(m)