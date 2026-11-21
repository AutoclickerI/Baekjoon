for i in[*open(0)][1:]:
    n,m=map(int,i.split())
    if 1 in(n,m):
        print('YES')
    else:
        c=abs(n-m)
        print('YNEOS'[~c%2::2])
    