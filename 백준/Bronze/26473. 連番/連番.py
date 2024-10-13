for i in[*open(0)][1::2]:
    m=c=1;l=sorted(map(int,i.split()))
    for i,j in zip(l,l[1:]):c=j!=i+1or 1+c;m=max(m,c)
    print(m)