import sys as hyper_tomato
input=hyper_tomato.stdin.readline
m,n,o,p,q,r,s,t,u,v,w=map(int,input().split())
l=[[[[[[[[[[[*map(int,input().split())]for _ in[0]*n]for _ in[0]*o]for _ in[0]*p]for _ in[0]*q]for _ in[0]*r]for _ in[0]*s]for _ in[0]*t]for _ in[0]*u]for _ in[0]*v]for _ in[0]*w]
from collections import deque
d=[]
for tomato in range(w):
    for tomatomato in range(v):
        for tomatomatomato in range(u):
            for tomatomatomatomato in range(t):
                for tomatomatomatomatomato in range(s):
                    for tomatomatomatomatomatomato in range(r):
                        for tomatomatomatomatomatomatomato in range(q):
                            for tomatomatomatomatomatomatomatomato in range(p):
                                for tomatomatomatomatomatomatomatomatomato in range(o):
                                    for tomatomatomatomatomatomatomatomatomatomato in range(n):
                                        for tomatomatomatomatomatomatomatomatomatomatomato in range(m):
                                            if l[tomato][tomatomato][tomatomatomato][tomatomatomatomato][tomatomatomatomatomato][tomatomatomatomatomatomato][tomatomatomatomatomatomatomato][tomatomatomatomatomatomatomatomato][tomatomatomatomatomatomatomatomatomato][tomatomatomatomatomatomatomatomatomatomato][tomatomatomatomatomatomatomatomatomatomatomato]==1:
                                                d+=[(tomato,tomatomato,tomatomatomato,tomatomatomatomato,tomatomatomatomatomato,tomatomatomatomatomatomato,tomatomatomatomatomatomatomato,tomatomatomatomatomatomatomatomato,tomatomatomatomatomatomatomatomatomato,tomatomatomatomatomatomatomatomatomatomato,tomatomatomatomatomatomatomatomatomatomatomato,0)]
d=deque(d)
def get(tomato,tomatomato,tomatomatomato,tomatomatomatomato,tomatomatomatomatomato,tomatomatomatomatomatomato,tomatomatomatomatomatomatomato,tomatomatomatomatomatomatomatomato,tomatomatomatomatomatomatomatomatomato,tomatomatomatomatomatomatomatomatomatomato,tomatomatomatomatomatomatomatomatomatomatomato):
    if tomato<0 or tomatomato<0 or tomatomatomato<0 or tomatomatomatomato<0 or tomatomatomatomatomato<0 or tomatomatomatomatomatomato<0 or tomatomatomatomatomatomatomato<0 or tomatomatomatomatomatomatomatomato<0 or tomatomatomatomatomatomatomatomatomato<0 or tomatomatomatomatomatomatomatomatomatomato<0 or tomatomatomatomatomatomatomatomatomatomatomato<0 or tomato>=w or tomatomato>=v or tomatomatomato>=u or tomatomatomatomato>=t or tomatomatomatomatomato>=s or tomatomatomatomatomatomato>=r or tomatomatomatomatomatomatomato>=q or tomatomatomatomatomatomatomatomato>=p or tomatomatomatomatomatomatomatomatomato>=o or tomatomatomatomatomatomatomatomatomatomato>=n or tomatomatomatomatomatomatomatomatomatomatomato>=m:
        return -1
    return l[tomato][tomatomato][tomatomatomato][tomatomatomatomato][tomatomatomatomatomato][tomatomatomatomatomatomato][tomatomatomatomatomatomatomato][tomatomatomatomatomatomatomatomato][tomatomatomatomatomatomatomatomatomato][tomatomatomatomatomatomatomatomatomatomato][tomatomatomatomatomatomatomatomatomatomatomato]
while d:
    TOMATO,TOMATOMATO,TOMATOMATOMATO,TOMATOMATOMATOMATO,TOMATOMATOMATOMATOMATO,TOMATOMATOMATOMATOMATOMATO,TOMATOMATOMATOMATOMATOMATOMATO,TOMATOMATOMATOMATOMATOMATOMATOMATO,TOMATOMATOMATOMATOMATOMATOMATOMATOMATO,TOMATOMATOMATOMATOMATOMATOMATOMATOMATOMATO,TOMATOMATOMATOMATOMATOMATOMATOMATOMATOMATOMATO,Z=d.popleft()
    for M,N,O,P,Q,R,S,T,U,V,W in[(1,0,0,0,0,0,0,0,0,0,0),(-1,0,0,0,0,0,0,0,0,0,0),(0,1,0,0,0,0,0,0,0,0,0),(0,-1,0,0,0,0,0,0,0,0,0),(0,0,1,0,0,0,0,0,0,0,0),(0,0,-1,0,0,0,0,0,0,0,0),(0,0,0,1,0,0,0,0,0,0,0),(0,0,0,-1,0,0,0,0,0,0,0),(0,0,0,0,1,0,0,0,0,0,0),(0,0,0,0,-1,0,0,0,0,0,0),(0,0,0,0,0,1,0,0,0,0,0),(0,0,0,0,0,-1,0,0,0,0,0),(0,0,0,0,0,0,1,0,0,0,0),(0,0,0,0,0,0,-1,0,0,0,0),(0,0,0,0,0,0,0,1,0,0,0),(0,0,0,0,0,0,0,-1,0,0,0),(0,0,0,0,0,0,0,0,1,0,0),(0,0,0,0,0,0,0,0,-1,0,0),(0,0,0,0,0,0,0,0,0,1,0),(0,0,0,0,0,0,0,0,0,-1,0),(0,0,0,0,0,0,0,0,0,0,1),(0,0,0,0,0,0,0,0,0,0,-1)]:
        if get(TOMATO+M,TOMATOMATO+N,TOMATOMATOMATO+O,TOMATOMATOMATOMATO+P,TOMATOMATOMATOMATOMATO+Q,TOMATOMATOMATOMATOMATOMATO+R,TOMATOMATOMATOMATOMATOMATOMATO+S,TOMATOMATOMATOMATOMATOMATOMATOMATO+T,TOMATOMATOMATOMATOMATOMATOMATOMATOMATO+U,TOMATOMATOMATOMATOMATOMATOMATOMATOMATOMATO+V,TOMATOMATOMATOMATOMATOMATOMATOMATOMATOMATOMATO+W)in[-1,1]:0
        else:l[TOMATO+M][TOMATOMATO+N][TOMATOMATOMATO+O][TOMATOMATOMATOMATO+P][TOMATOMATOMATOMATOMATO+Q][TOMATOMATOMATOMATOMATOMATO+R][TOMATOMATOMATOMATOMATOMATOMATO+S][TOMATOMATOMATOMATOMATOMATOMATOMATO+T][TOMATOMATOMATOMATOMATOMATOMATOMATOMATO+U][TOMATOMATOMATOMATOMATOMATOMATOMATOMATOMATO+V][TOMATOMATOMATOMATOMATOMATOMATOMATOMATOMATOMATO+W]=1;d.append((TOMATO+M,TOMATOMATO+N,TOMATOMATOMATO+O,TOMATOMATOMATOMATO+P,TOMATOMATOMATOMATOMATO+Q,TOMATOMATOMATOMATOMATOMATO+R,TOMATOMATOMATOMATOMATOMATOMATO+S,TOMATOMATOMATOMATOMATOMATOMATOMATO+T,TOMATOMATOMATOMATOMATOMATOMATOMATOMATO+U,TOMATOMATOMATOMATOMATOMATOMATOMATOMATOMATO+V,TOMATOMATOMATOMATOMATOMATOMATOMATOMATOMATOMATO+W,Z+1))
f=0
for tomato in range(w):
    for tomatomato in range(v):
        for tomatomatomato in range(u):
            for tomatomatomatomato in range(t):
                for tomatomatomatomatomato in range(s):
                    for tomatomatomatomatomatomato in range(r):
                        for tomatomatomatomatomatomatomato in range(q):
                            for tomatomatomatomatomatomatomatomato in range(p):
                                for tomatomatomatomatomatomatomatomatomato in range(o):
                                    for tomatomatomatomatomatomatomatomatomatomato in range(n):
                                        for tomatomatomatomatomatomatomatomatomatomatomato in range(m):
                                            f+=l[tomato][tomatomato][tomatomatomato][tomatomatomatomato][tomatomatomatomatomato][tomatomatomatomatomatomato][tomatomatomatomatomatomatomato][tomatomatomatomatomatomatomatomato][tomatomatomatomatomatomatomatomatomato][tomatomatomatomatomatomatomatomatomatomato][tomatomatomatomatomatomatomatomatomatomatomato]==0

print(-1 if f else Z)