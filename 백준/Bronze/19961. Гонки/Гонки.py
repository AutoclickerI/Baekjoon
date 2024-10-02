a,b,c,d,e=map(int,open(0).read().split())
def f(x,y):q,r=divmod(e-1,x*y);return q*2*x-~r/y
g=f(a,b)-f(c,d)
print('Second'*(g>0)or'First'*(g<0)or'Draw')