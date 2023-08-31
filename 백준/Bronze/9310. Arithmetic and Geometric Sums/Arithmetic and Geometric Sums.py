*l,_=map(int,open(0).read().split())
while l:n,a,b,c,*l=l;print(((a+c==2*b)*(2*a+~-n*(b-a))*n//2)or((b//a)**n-1)//(b//a-1)*a)