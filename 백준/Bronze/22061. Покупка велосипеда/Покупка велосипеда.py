for i in[*open(0)][1:]:
    p,q,r=map(int,i.split())
    print('NYOE S'[(p or r%2==0)and p+2*q>=r::2])