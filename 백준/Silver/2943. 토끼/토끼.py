[N,M],*l=[map(int,i.split())for i in open(0)]
import math
blk=math.isqrt(N)
blocks=[0]*((N+blk-1)//blk)
mat=[0]*N

for S,A in l:
    A-=1
    nA=(A+blk-1)//blk*blk
    r=0
    if S<nA-A:
        for i in range(S):
            mat[i+A]+=1
            r+=mat[i+A]
        print(r)
    else:
        for i in range(A,nA):
            mat[i]+=1
            r+=mat[i]
            S-=1
        i=nA//blk
        while blk<=S:
            blocks[i]+=1
            r+=blocks[i]
            S-=blk
            i+=1
        if S and i*blk+S==N:
            blocks[-1]+=1
            r+=blocks[-1]
        else:
            for j in range(S):
                mat[i*blk+j]+=1
                r+=mat[i*blk+j]
        print(r)