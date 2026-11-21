[_,k,x,y],*a=(map(int,i.split())for i in open(0))
print(sum(k*k<(p-x)**2+(q-y)**2for p,q in a))