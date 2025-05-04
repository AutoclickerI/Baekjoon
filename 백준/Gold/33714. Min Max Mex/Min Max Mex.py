N,K=map(int,input().split())
A=sorted(map(int,input().split()))


m=1e18
d={}
for i in A:d[i]=d.get(i,0)+1

sd=sorted(d)

if 0 not in d:
    m=0

for i in sd:
    if d[i]<=K:
        m=min(m,i)
    if i+1 not in d:
        m=min(m,i+1)
    p=i

i=0
if A[0] and K:
    A=[0,*A]
    K-=1

while i<len(A)-1:
    if A[i]==A[i+1]:
        i+=1
        continue
    else:
        if K>=A[i+1]-A[i]-1:
            K-=A[i+1]-A[i]-1
            i+=1
        else:
            break

if A[0]:
    print(m,0)
else:
    print(m,A[i]+K+1)