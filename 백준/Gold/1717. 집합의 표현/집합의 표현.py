import sys
sys.setrecursionlimit(9**9)

(N,M),*l=[map(int,i.split())for i in open(0)]
*v,=range(N+1)

def find(n):
    if v[n]-n:
        v[n]=find(v[n])
    return v[n]
def union(s,e):
    s=find(s)
    e=find(e)
    v[s]=v[e]=min(s,e)

for q,i,j in l:
    if q:
        print('YNEOS'[find(i)!=find(j)::2])
    else:
        union(i,j)