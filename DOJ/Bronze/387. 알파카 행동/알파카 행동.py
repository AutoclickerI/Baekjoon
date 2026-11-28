_,*l=map(int,open(0))
for a,g in zip(*[iter(l)]*2):
    d=abs(a-g)
    print('He is',['a fake','similar','a real'][(d<4)+(d<1)],'alpaca')