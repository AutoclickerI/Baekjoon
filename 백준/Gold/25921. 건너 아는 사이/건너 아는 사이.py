N=int(input())
*l,=range(N+1)
for i in range(2,N+1):
    if l[i]==i:
        t=2*i
        while t<N+1:
            l[t]=min(l[t],i)
            t+=i
print(sum(l)-1)