N,*l=map(int,open(0).read().split())
p,q=min(l[1::2]),min(l[2::2])
print(min(N*q,N//6*p+N%6*q,N//-6*-p))