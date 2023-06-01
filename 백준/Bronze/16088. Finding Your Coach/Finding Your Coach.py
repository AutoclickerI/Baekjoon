for i in[*open(0)][1:]:
    p,q,r,s=map(int,i.split())
    d=abs(r-s)
    if r==s:print('G')
    elif p>=d<=q:print('E')
    elif d<=q:print('R')
    else:print('L')