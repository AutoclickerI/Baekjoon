X,Y,c=map(int,input().split())
Z=X*X+Y*Y
print((0<Z<c*c)-int(Z**.5//-c))