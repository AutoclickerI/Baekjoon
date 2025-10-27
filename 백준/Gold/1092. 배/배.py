[N],c,[p],l=[sorted(map(int,i.split()))for i in open(0)]

x=[[]for _ in[0]*N]
i=0
try:
    for v in l:
        while c[i]<v:
            i+=1
        x[i]+=v,
    t=0
    while p:
        for i in range(N)[::-1]:
            if p<1:continue
            while x[i]==[]:i-=1
            if i<0:continue
            x[i].pop()
            p-=1
        t+=1
    print(t)
except:
    print(-1)