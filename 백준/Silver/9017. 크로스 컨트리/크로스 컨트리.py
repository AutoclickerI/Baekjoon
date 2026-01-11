for i in[*open(0)][2::2]:
    d={}
    c={}
    l={}
    for v in i.split():
        d[v]=d.get(v,0)+1
    j=0
    dd={**d}
    for v in i.split():
        if d[v]==6:
            j+=1
            c[v]=c.get(v,0)+j*(2<dd[v])
            dd[v]-=1
            if dd[v]:
                l[v]=j
    print(min(c,key=lambda i:(c[i],l[i])))