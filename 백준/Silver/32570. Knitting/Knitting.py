N,K,P=map(int,input().split())
input()
*l,=map(int,input().split())
s={*range(1,K+1)}
d={}
cd={}
for idx,i in enumerate(l):
    d[i]=idx
    s.discard(i)
    cd[i]=cd.get(i,0)+1
for i in s:
    idx+=1
    l+=i,
    d[i]=idx
    cd[i]=1
sd=sorted(d,key=d.get)
minval=min(cd.values())
while len(l)<N:
    for i in sd:
        if cd[i]==minval:
            l+=i,
            cd[i]+=1
    minval+=1
l=l[:N]
d={}
f=1
for idx,i in enumerate(l):
    if i in d:
        f&=P<=idx-d[i]
    d[i]=idx
print(*f*l or['impossible'])