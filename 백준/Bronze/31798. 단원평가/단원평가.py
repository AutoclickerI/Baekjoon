p,q,r=map(int,input().split())
print([r*r-max(p,q),int((p+q)**.5)][0<p*q])