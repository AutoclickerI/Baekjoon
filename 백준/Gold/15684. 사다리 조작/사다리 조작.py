import sys
sys.setrecursionlimit(2*10**5)
input=sys.stdin.readline

N,M,H=map(int,input().split())
b=[~-N*[0]for _ in[0]*H]

def simulate():
    *l,=range(N)
    for i in b:
        for j in range(N-1):
            if i[j]:l[j:j+2]=l[j+1],l[j]
    return l==[*range(N)]

for _ in[0]*M:
    y,x=map(int,input().split())
    b[y-1][x-1]=1

if simulate():
    exit(print(0))
from itertools import*

for i in*combinations(range(~-N*H),1),*combinations(range(~-N*H),2),*combinations(range(~-N*H),3):
    ii=[(v//(N-1),v%(N-1))for v in i]
    tmp=[]
    for y,x in ii:
        if b[y][x]:
            continue
        if 0<x and b[y][x-1]==1:
            continue
        if x<N-2 and b[y][x+1]==1:
            continue
        b[y][x]=1
        tmp+=(y,x),
    if simulate():
        exit(print(len(i)))
    for y,x in tmp:
        b[y][x]=0
print(-1)