N,M=map(int,input().split())
l=[]
for _ in[0]*M:
    A,B=map(int,input().split())
    l+=[*'+'*A+'-'*B],
i=idx=0
while idx<M:
    while len(l[idx])<N:
        if len(l[idx])<i:
            l[idx].insert(i,'-')
        else:
            l[idx].insert(i,'-X'[i<N])
            i+=1
    idx+=1
if i<N or any(N<len(i)for i in l):
    print('NO')
else:
    print('YES')
    for ii in zip(*l):print(*ii,sep='')