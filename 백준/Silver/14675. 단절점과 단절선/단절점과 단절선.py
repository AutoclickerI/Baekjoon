import sys
input=sys.stdin.readline

d={}
n=int(input())
edges=[[*map(int,input().split())]for _ in[0]*~-n]
for i in edges:
    for j in i:
        d[j]=d.get(j,0)+1

for _ in[0]*int(input()):
    q,n=map(int,input().split())
    if q-1:
        print('yes')
    else:
        print('yneos'[d[n]<2::2])