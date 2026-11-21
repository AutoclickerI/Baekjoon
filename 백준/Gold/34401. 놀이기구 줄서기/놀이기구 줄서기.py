(N,P,K),*l=[[*map(int,i.split())]for i in open(0)]
q=[[]for _ in[0]*6]
for t,a in sorted(l):q[a]+=t,
for i in range(6):q[i]=q[i][::-1]
delay=i=0
while N:
    t=i*P
    possible=K
    while 1:
        m=[(q[j][-1],j)for j in range(6)if q[j] and j<=possible and q[j][-1]<=t]
        if not m:
            break
        _,j=min(m)
        possible-=j
        delay+=t-q[j].pop()
        N-=1
    i+=1
print(delay)