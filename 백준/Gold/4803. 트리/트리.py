import sys
input=sys.stdin.readline

def find(n):
    if p[n]!=n:
        p[n]=find(p[n])
    return p[n]

def union(a,b):
    a,b=sorted([find(a),find(b)])
    if a==b:
        t[a]=0
    else:
        p[b]=a
        t[a]=min(t[a],t[b])

T=0
while'1'<(s:=input()):
    T+=1
    n,m=map(int,s.split())
    *p,=range(n+1)
    t=[1]*-~n
    for _ in[0]*m:
        a,b=map(int,input().split())
        union(a,b)
    s={find(i)for i in range(1,n+1)}
    a=sum(t[i]for i in s)
    print(f'Case {T}:')
    if a==0:
        print('No trees.')
    elif a==1:
        print('There is one tree.')
    else:
        print('A forest of',a,'trees.')