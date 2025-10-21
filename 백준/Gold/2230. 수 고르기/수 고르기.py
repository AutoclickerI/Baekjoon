N,M,*l=map(int,open(0).read().split())
l.sort()
i=j=0
m=9e9
while i<N:
    while j<N and l[j]-l[i]<M:
        j+=1
    if i<=j<N and M<=l[j]-l[i]:
        m=min(m,l[j]-l[i])
    i+=1
print(m)