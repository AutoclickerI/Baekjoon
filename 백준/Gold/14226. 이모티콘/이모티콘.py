S=int(input())
d={(1,0):0}

l=[(0,1,0)]

for c,v,p in l:
    if v==S:
        exit(print(c))
    for nv,np in(v,v),(v+p,p),(v-1,p):
        if(nv,np)not in d:
            d[nv,np]=c+1
            l+=(c+1,nv,np),