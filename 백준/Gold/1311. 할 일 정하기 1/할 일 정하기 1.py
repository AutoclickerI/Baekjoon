[N],*b=[[*map(int,i.split())]for i in open(0)]
d={0:0}
for x in b:
    t={}
    for n in d:
        for i,v in enumerate(x):
            if(1<<i)&n<1:
                nn=n|(1<<i)
                t[nn]=min(t.get(nn,1e9),d[n]+v)
    d=t
print(d[2**N-1])