[N],*b=[[*map(int,i.split())]for i in open(0)]
m=float('inf')

for i in range(1,2**N-1):
    v=0
    t1=[]
    t2=[]
    for x in range(N):
        if i%2:
            t1+=x,
        else:
            t2+=x,
        i//=2
    for i in t1:
        for j in t1:
            v+=b[i][j]
    for i in t2:
        for j in t2:
            v-=b[i][j]
    m=min(m,abs(v))
print(m)