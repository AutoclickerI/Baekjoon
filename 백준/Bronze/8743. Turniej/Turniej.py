for i in[*open(0)][1:]:
    p,q=map(int,i.split())
    print(min(p,q-1))