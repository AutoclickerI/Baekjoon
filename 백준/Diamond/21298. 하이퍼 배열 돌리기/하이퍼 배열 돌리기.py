import sys
from itertools import*

input=sys.stdin.readline

M,N,O,P,Q,R,S,T,U,V,W=dims=[*map(int,input().split())]
A=[[[[[[[[[[[*map(int,input().split())]for _ in[0]*V]for _ in[0]*U]for _ in[0]*T]for _ in[0]*S]for _ in[0]*R]for _ in[0]*Q]for _ in[0]*P]for _ in[0]*O]for _ in[0]*N]for _ in[0]*M]
pairs=[(i,j)for i in range(11)for j in range(i+1,11)]
*perm,=range(11)

def getv(coord):
    m,n,o,p,q,r,s,t,u,v,w=coord
    return A[m][n][o][p][q][r][s][t][u][v][w]

def setv(coord,val):
    m,n,o,p,q,r,s,t,u,v,w=coord
    A[m][n][o][p][q][r][s][t][u][v][w]=val

for _ in[0]*int(input()):
    op,*l=map(int,input().split())
    if 66<op:
        a,b=pairs[op-67]
        perm[a],perm[b]=perm[b],perm[a]
        continue

    L=[0]*11
    R=[0]*11
    for lg in range(11):
        p=perm[lg]
        L[p]=l[lg]-1
        R[p]=l[11+lg]-1

    if op<12:
        p=perm[op-1]
        others=[i for i in range(11)if i!=p]

        for fixed in product(*[range(L[i],R[i]+1)for i in others]):
            coord=L[:]
            for ax,v in zip(others,fixed):
                coord[ax]=v

            x=L[p]
            y=R[p]
            while x<y:
                coord[p]=x
                vx=getv(coord)
                coord[p]=y
                vy=getv(coord)
                coord[p]=x
                setv(coord,vy)
                coord[p]=y
                setv(coord,vx)
                x+=1
                y-=1

    else:
        la,lb=pairs[op-12]
        p=perm[la]
        q=perm[lb]
        others=[i for i in range(11)if i!=p and i!=q]

        for fixed in product(*[range(L[i],R[i]+1)for i in others]):
            base=L[:]
            for ax,v in zip(others,fixed):
                base[ax]=v

            for d in range(min(R[p]-L[p]+1,R[q]-L[q]+1)//2):
                left=L[p]+d
                right=R[p]-d
                top=L[q]+d
                bottom=R[q]-d

                ring=[]

                for x in range(left,right+1):
                    c=base[:]
                    c[p]=x
                    c[q]=top
                    ring+=c,

                for y in range(top+1,bottom+1):
                    c=base[:]
                    c[p]=right
                    c[q]=y
                    ring+=c,

                for x in range(right-1,left-1,-1):
                    c=base[:]
                    c[p]=x
                    c[q]=bottom
                    ring+=c,

                for y in range(bottom-1,top,-1):
                    c=base[:]
                    c[p]=left
                    c[q]=y
                    ring+=c,

                first=getv(ring[0])
                for i in range(len(ring)-1):
                    setv(ring[i],getv(ring[i+1]))
                setv(ring[-1],first)

dims=[dims[perm[i]]for i in range(11)]
print(*dims)

for it in product(*(range(dims[i])for i in range(10))):
    coord=[0]*11
    for lg in range(10):
        coord[perm[lg]]=it[lg]

    for x in range(dims[10]):
        coord[perm[10]]=x
        print(getv(coord))