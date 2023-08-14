a,b,c,d,e,f=map(int,open(0).read().split())
p=3*a+20*b+120*c
q=3*d+20*e+120*f
if p==q:
    print('Draw')
if p>q:
    print('Max')
if p<q:
    print('Mel')