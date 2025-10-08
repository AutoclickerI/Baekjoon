for i in[*open(0)][2::2]:
    l=0,*map(int,i.split())
    v=[0]*len(l)
    c=0
    for i in range(len(l)):
        if v[i]<1:
            c+=1
            while v[i]<1:
                v[i]=1
                i=l[i]
    print(c-1)