N,M,D=map(int,input().split())
o=[[*map(int,input()[::2])]for _ in[0]*N]

from itertools import*

m=0
for i,j,k in combinations(range(M),3):
    b=[[*i]for i in o]
    cnt=0
    try:
        while 1:
            _,mxi,myi=min((abs(x-i)-y,x,y)for y in range(N)for x in range(M)if b[y][x])
            _,mxj,myj=min((abs(x-j)-y,x,y)for y in range(N)for x in range(M)if b[y][x])
            _,mxk,myk=min((abs(x-k)-y,x,y)for y in range(N)for x in range(M)if b[y][x])
            if abs(i-mxi)+N-myi<=D:
                cnt+=b[myi][mxi]
                b[myi][mxi]=0
            if abs(j-mxj)+N-myj<=D:
                cnt+=b[myj][mxj]
                b[myj][mxj]=0
            if abs(k-mxk)+N-myk<=D:
                cnt+=b[myk][mxk]
                b[myk][mxk]=0
            b=M*[0],*b[:-1]
    except:
        pass
    m=max(m,cnt)
print(m)