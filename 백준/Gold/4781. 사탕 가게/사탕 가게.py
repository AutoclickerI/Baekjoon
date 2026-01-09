import sys
input=sys.stdin.readline

while'1'<(s:=input()):
    n,m=map(int,s.replace('.','').split())
    v=[0]*-~m
    for _ in[0]*n:
        c,p=map(int,input().replace('.','').split())
        for i in range(p,m+1):
            v[i]=max(v[i],v[i-p]+c)
    print(max(v))