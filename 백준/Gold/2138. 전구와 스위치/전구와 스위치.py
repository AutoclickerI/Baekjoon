input()
l=[i!=j for i,j in zip(input(),input())]

m=float('inf')

v=1

ll=l[:]
ll[0]^=1
ll[1]^=1
for i in range(1,len(ll)):
    if ll[i-1]:
        ll[i-1]^=1
        ll[i]^=1
        if i+1<len(ll):
            ll[i+1]^=1
        v+=1
if sum(ll)<1:
    m=min(m,v)
v=0
for i in range(1,len(l)):
    if l[i-1]:
        l[i-1]^=1
        l[i]^=1
        if i+1<len(l):
            l[i+1]^=1
        v+=1
if sum(l)<1:
    m=min(m,v)
print(-(m==float('inf'))or m)