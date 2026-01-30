N,K=map(int,input().split())
v=['?']*N
p=0
for _ in[0]*K:
    d,c=input().split()
    p=(p-int(d))%N
    if v[p]=='?':
        v[p]=c
    elif v[p]!=c:
        print('!')
        break
else:
    for i in{*v}-{'?'}:
        if 1<v.count(i):
            print('!')
            break
    else:
        print(*(v*2)[p:p+N],sep='')