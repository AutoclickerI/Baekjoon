[N,M],*l=[map(int,i.split())for i in open(0)]

tr=[0]*N
for q,i,*x in l:
    i-=1
    if q==1:
        tr[i]|=1<<x[0]-1
    if q==2:
        tr[i]&=(2**20-1)^(1<<x[0]-1)
    if q==3:
        tr[i]=tr[i]<<1&(2**20-1)
    if q==4:
        tr[i]>>=1
print(len({*tr}))