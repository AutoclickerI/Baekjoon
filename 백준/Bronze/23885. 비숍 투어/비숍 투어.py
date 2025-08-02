N,M,a,b,c,d=map(int,open(0).read().split())
if (a+b-c-d)//2:
    print('YNEOS'[1 in(N,M,(a+b-c-d)%2)::2])
else:
    print('YNEOS'[(a+b-c-d)%2::2])