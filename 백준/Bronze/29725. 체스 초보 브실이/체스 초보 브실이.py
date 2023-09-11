P,p,N,n,B,b,R,r,Q,q=map(open(0).read().count,'PpNnBbRrQq')
print(P-p+3*(N+B-n-b)+5*(R-r)+9*(Q-q))