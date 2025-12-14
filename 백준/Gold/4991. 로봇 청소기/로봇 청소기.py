import sys
input=sys.stdin.readline

from itertools import*

def BFS(s,e):
    v=[w*[0]for _ in[0]*h]
    l=[(0,*s)]
    for c,y,x in l:
        if(y,x)==e:
            return c
        for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
            ny,nx=y+dy,x+dx
            if 0<=ny<h and 0<=nx<w and v[ny][nx]<1 and b[ny][nx]!='x':
                v[ny][nx]=1
                l+=(c+1,ny,nx),
    return-1

while'1'<(s:=input()):
    w,h=map(int,s.split())
    b=[input()for _ in[0]*h]
    l=[]
    for y in range(h):
        for x in range(w):
            if b[y][x]=='*':
                l+=(y,x),
            if b[y][x]=='o':
                st=y,x
    a=float('inf')
    dm={}
    for arr in permutations(l):
        r=0
        for s,e in zip([st,*arr],arr):
            if(s,e)in dm:
                dist=dm[s,e]
            else:
                dist=BFS(s,e)
                dm[s,e]=dm[e,s]=dist
            if dist<0:
                r=-1
            if-1<r:
                r+=dist
            if a<r:break
        a=min(a,r)
    print(a)