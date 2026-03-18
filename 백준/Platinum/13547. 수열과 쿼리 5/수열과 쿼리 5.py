import math

[N],A,[Q],*l=[[*map(int,i.split())]for i in open(0)]

blk=math.isqrt(N)

cnt=[0]*1000001
df=0

def push(i):
    global df
    df+=cnt[i]==0
    cnt[i]+=1

def pop(i):
    global df
    cnt[i]-=1
    df-=cnt[i]==0

sl=sorted(l,key=lambda i:(i[0]//blk,i[1]))

ps=0
pe=0
d={}
for s,e in sl:
    s-=1
    while pe<e:
        push(A[pe])
        pe+=1
    while e<pe:
        pe-=1
        pop(A[pe])
    while ps<s:
        pop(A[ps])
        ps+=1
    while s<ps:
        ps-=1
        push(A[ps])
    d[s+1,e]=df

for s,e in l:print(d[s,e])