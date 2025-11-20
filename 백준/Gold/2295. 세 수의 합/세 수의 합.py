N,*l=map(int,open(0))

s1=set()
for i in range(N):
    for j in range(i,N):
        s1.add(l[i]+l[j])

s2={}
for i in range(N):
    for j in range(i,N):
        v=l[i]-l[j]
        if v<0:
            s2[v]=max(s2.get(v,0),l[j])

m=0
for i in s2:
    if-i in s1:m=max(m,s2[i])
print(m)