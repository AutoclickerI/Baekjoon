N,K,*l=map(int,open(0).read().split())
m=c=0
i=j=0
while j<N:
    while 0<=K and j<N:
        if l[j]%2:
            K-=1
        else:
            c+=1
            m=max(m,c)
        j+=1
    while K<0:
        if l[i]%2:
            K+=1
        else:
            c-=1
        i+=1
print(m)