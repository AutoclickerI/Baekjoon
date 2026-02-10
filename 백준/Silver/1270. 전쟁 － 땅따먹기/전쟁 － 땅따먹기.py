for i in[*open(0)][1:]:
    n,*l=i.split()
    d={}
    for i in l:d[i]=d.get(i,0)+1
    md=max(d.values())
    if int(n)<md*2:
        print(*[i for i in d if d[i]==md])
    else:
        print('SYJKGW')