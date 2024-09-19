n,m,s,*l=map(int,open(0).read().split())
possible={s:0}
for i in l:
    tmp={}
    for j in possible:
        if j+i+1<=m:
            # in-line
            tmp[j+i+1]=min(possible[j],tmp.get(j+i+1,10**9))
        # newline
        tmp[i]=min(possible[j]+(m-j)**2,tmp.get(i,10**9))
    possible=tmp
print(min(possible.values()))