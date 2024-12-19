for i in[*open(0)][:-1]:
    _,*l=i.split()
    a=[l[0]]
    for i,j in zip(l,l[1:]):a+=[j]*(i!=j)
    print(*a,'$')