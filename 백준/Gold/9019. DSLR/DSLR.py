from collections import deque
for i in[*open(0)][1:]:
    p,q=map(int,i.split())
    Q=deque([(x:=p,'')])
    v=[0]*20000
    while x-q:
        x,y=Q.popleft()
        for i,j in zip(l:=[x*2%10000,(x-1)%10000,10*x//10000+10*x%10000,x%10*1000+x//10],'DSLR'):
            if v[i]:continue
            Q.append((i,y+j))
            v[i]=1
    print(y)