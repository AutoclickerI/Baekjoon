*dice,=map(int,input().split())

nn=[*range(1,22),-1,23,24,30,26,30,28,29,30,31,32,20,-1]
sn=nn[:]
sn[5]=22
sn[10]=25
sn[15]=27
ss=*range(0,42,2),0,13,16,19,22,24,28,27,26,25,30,35,40,0
mr=0

for i in range(4**10):
    v=[0]*4
    mv=[]
    r=0
    for _ in range(10):
        mv+=i%4,
        i//=4
    for num,mov in zip(mv,dice):
        if v[num]==-1:
            break
        v[num]=sn[v[num]]
        for _ in[0]*~-mov:
            v[num]=nn[v[num]]
        r+=ss[v[num]]
        if v[num]!=-1:
            for ii in range(4):
                if ii==num:
                    continue
                if v[ii]==v[num]:
                    break
            else:
                continue
            break
    else:
        mr=max(mr,r)
print(mr)