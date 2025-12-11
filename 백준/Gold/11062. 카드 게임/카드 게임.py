import sys
input=sys.stdin.readline

for _ in[0]*int(input()):
    N=int(input())
    *l,=map(int,input().split())
    ss=sum(l)
    if N%2:
        val=[-i for i in l]
        s=1
    else:
        val=l[:]
        s=-1
    for d in range(1,N):
        tmp=[(1-2*s)*float('inf')]*N
        if s==1:
            fun=max
        else:
            fun=min
        for i in range(N-d):
            tmp[i]=fun(tmp[i],val[i+1]+l[i]*s)
        for i in range(d,N):
            tmp[i-d]=fun(tmp[i-d],val[i-d]+l[i]*s)
        s*=-1
        val=tmp
    print(ss-val[0]>>1)