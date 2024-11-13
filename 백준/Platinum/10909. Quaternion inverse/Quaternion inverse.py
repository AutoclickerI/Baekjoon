p,q,*l=map(int,open(0).read().split())
for i in range(q):a,b,c,d=l[4*i:4*-~i];H=a*a+b*b+c*c+d*d;print(*[H%p and-i*pow(H,-1,p)for i in[-a,b,c,d]])