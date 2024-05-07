p,q,r=map(int,input().split())
print([r*r-p-q,int((p+q)**.5)][0<p*q])