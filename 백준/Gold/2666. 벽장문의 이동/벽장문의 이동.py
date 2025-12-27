[N],s,_,*l=[sorted(map(int,i.split()))for i in open(0)if'0'<i]
c=[(0,*s)]
for[v]in l:
    t=[]
    for co,s,e in c:
        if v<e:
            t+=(co+abs(v-s),v,e),
        if s<v:
            t+=(co+abs(v-e),s,v),
    c=t
print(min(c)[0])