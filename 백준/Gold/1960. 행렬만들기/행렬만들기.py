[N],A,B=[[*map(int,i.split())]for i in open(0)]
try:
    l=[(v,i)for i,v in enumerate(B)]
    x=[1]
    for i in A:
        l.sort()
        r=[]
        while len(r)<i:
            v,j=l.pop()
            if v:
                r+=(j,v),
        s=['0']*N
        for j,v in r:
            s[j]='1'
            l+=(v-1,j),
        x+=''.join(s),
    assert all(i<1 for i,_ in l)
    print(*x,sep='\n')
except:
    print(-1)