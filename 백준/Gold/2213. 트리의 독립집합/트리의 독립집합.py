import sys
sys.setrecursionlimit(2*10**5)
#input=sys.stdin.readline

[n],w,*l=[[*map(int,i.split())]for i in open(0)]

edges=[[]for _ in[0]*n]

for s,e in l:
    edges[s-1]+=e-1,
    edges[e-1]+=s-1,

v=[0]*n
z=[0]*n
o=[0]*n
li_z=[[]for _ in[0]*n]
li_o=[[]for _ in[0]*n]

def DFS(n):
    v[n]=1
    acc_z=0
    acc_o=0
    li_ot=[]
    li_zt=[]
    for e in edges[n]:
        if v[e]<1:
            DFS(e)
            acc_o+=o[e]
            li_ot+=li_o[e]
            acc_z+=z[e]
            li_zt+=li_z[e]
    z[n]=acc_o
    li_z[n]=li_ot
    o[n]=w[n]+acc_z
    li_o[n]=[n]+li_zt
    if o[n]<acc_o:
        o[n]=acc_o
        li_o[n]=li_ot

DFS(0)
print(o[0])
print(*[i+1 for i in sorted(li_o[0])])