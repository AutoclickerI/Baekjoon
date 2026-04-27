import sys
input=sys.stdin.readline

N=int(input())
l=input().split()

edges={i:[]for i in l}
deg={i:0 for i in l}
ch={i:[]for i in l}

for _ in[0]*int(input()):
    x,y=input().split()
    edges[y]+=x,
    deg[x]+=1

r=sorted(i for i in l if deg[i]<1)
q=r[:]

for n in q:
    for e in edges[n]:
        deg[e]-=1
        if deg[e]<1:
            ch[n]+=e,
            q+=e,

print(len(r),*r)

for n in sorted(l):
    ch[n].sort()
    print(n,len(ch[n]),*ch[n])