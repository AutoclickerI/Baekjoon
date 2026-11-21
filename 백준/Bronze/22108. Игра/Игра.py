f=lambda:[*map(int,input().split())]
g=lambda l:all(i-j for a in l for i,j in zip(a,a[1:]))
for _ in[0]*f()[0]:l=eval('f(),'*f()[0]);print('YNEOS'[all(map(all,l))and g(l)and g(zip(*l))::2])