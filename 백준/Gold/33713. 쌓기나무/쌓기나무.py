import sys
input=sys.stdin.readline

N,M,Q=map(int,input().split())
d={}
nd=0
F={}
nF=0
S={}
nS=0

for _ in[0]*Q:
    (_,q,*_),*l=input().split()
    if q in'TE':
        s=i,j=int(l[0]),int(l[1])
    if q=='T':
        d[i,j]=d.get(s,0)+1
        v=d[s]
        nd+=v==1
        x=F[i,v]=F.get((i,v),0)+1
        nF+=x==1
        x=S[j,v]=S.get((j,v),0)+1
        nS+=x==1
    if q=='E' and d.get(s):
        v=d[s]
        d[s]-=1
        F[i,v]-=1
        S[j,v]-=1
        nd-=d[s]<1
        nF-=F[i,v]<1
        nS-=S[j,v]<1
    if q=='O':print(nd)
    if q=='R':print(nF)
    if q=='I':print(nS) 