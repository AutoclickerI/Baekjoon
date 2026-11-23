import math

[N,K,Q],A,*l=[[*map(int,i.split())]for i in open(0)]
M=N+K-1
blk=math.isqrt(N)

S=[0]*M
for q in range(K,M):S[q]=S[q-K]+A[q-K+1]-A[q-K]
ix={}
V=[0]*M
for q in range(M):
    w=S[q]*K+q%K
    V[q]=ix[w]=ix.get(w,len(ix))
C=[q%K for q in range(M)]

cnt=[0]*len(ix)
cc=[0]*(M+2*K)
mx=[0]*K
tot=0

def push(q):
    global tot
    v=V[q];c=C[q]
    f=cnt[v]+1;cnt[v]=f
    cc[f*K+c]+=1
    cc[f*K+c-K]-=1
    if mx[c]<f:mx[c]=f;tot+=1

def pop(q):
    global tot
    v=V[q];c=C[q]
    f=cnt[v];cnt[v]=f-1
    cc[f*K+c]-=1
    cc[f*K+c-K]+=1
    if mx[c]==f and cc[f*K+c]==0:mx[c]=f-1;tot-=1

ps=pe=0
d={}
for s,e in sorted(l,key=lambda i:(i[0]//blk,i[1])):
    s-=1
    e+=K-1
    while pe<e:
        push(pe)
        pe+=1
    while e<pe:
        pe-=1
        pop(pe)
    while ps<s:
        pop(ps)
        ps+=1
    while s<ps:
        ps-=1
        push(ps)
    d[s+1,e-K+1]=e-s-tot

for s,e in l:print(d[s,e])