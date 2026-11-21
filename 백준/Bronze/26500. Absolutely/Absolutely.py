_,*l=map(eval,open(0).read().split())
while l:p,q,*l=l;print(f'{abs(p-q):.1f}')