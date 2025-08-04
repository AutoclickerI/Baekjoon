N,K,*l=map(int,open(0).read().split())

for i in range(N)[::-1]:
    for j in range(i):
        if l[j]>l[j+1]:
            K-=1
            l[j],l[j+1]=l[j+1],l[j]
            K<1<exit(print(*l))
print(-1)