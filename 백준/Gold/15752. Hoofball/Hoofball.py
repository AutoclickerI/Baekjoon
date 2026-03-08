N,*l=map(int,open(0).read().split())
l.sort()

if N<2:
    print(1)
    exit()

l.sort()

p=[-1]*N
p[0]=1
p[N-1]=N-2
for i in range(1,N-1):
    if l[i+1]-l[i]<l[i]-l[i-1]:
        p[i]=i+1
    else:
        p[i]=i-1

deg=[0]*N
for i in p:deg[i]+=1
r=0
for i in range(N):
    if i<p[i]and i==p[p[i]]and deg[i]==deg[p[i]]==1:
        r+=1
print(r+sum(i<1 for i in deg))