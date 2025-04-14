import sys
input=sys.stdin.readline

from collections import deque

for T in[0]*int(input()):
    H,W=map(int,input().split())
    W+=2
    b=['.'*W,*['.'+input().strip()+'.'for _ in[0]*H],'.'*W]
    H+=2
    v=[W*[0]for _ in[0]*H]
    keys=[0]*26
    for i in input().strip():
        if i=='0':break
        keys[ord(i)-97]=1
    d=[[]for _ in[0]*26]
    dq=deque()
    for i in range(W):
        dq+=(0,i),(H-1,i)
        v[0][i]=v[H-1][i]=1
    for i in range(1,H-1):
        dq+=(i,0),(i,W-1)
        v[i][0]=v[i][W-1]=1
    ans=0
    while dq:
        y,x=dq.popleft()
        for dy,dx in(-1,0),(1,0),(0,-1),(0,1):
            ny,nx=y+dy,x+dx
            if 0<=ny<H and 0<=nx<W and v[ny][nx]<1:
                c=b[ny][nx]
                if c=='*':
                    v[ny][nx]=1
                elif c in'.$':
                    ans+=c=='$'
                    v[ny][nx]=1
                    dq+=(ny,nx),
                elif c.isupper():
                    if keys[ord(c)-65]:
                        v[ny][nx]=1
                        dq+=(ny,nx),
                    else:
                        d[ord(c)-65]+=(ny,nx),
                        v[ny][nx]=1
                elif c.islower():
                    v[ny][nx]=1
                    keys[ord(c)-97]=1
                    dq+=d[ord(c)-97]
                    d[ord(c)-97]=[]
                    dq+=(ny,nx),
    print(ans)