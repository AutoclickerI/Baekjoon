a,b,S=map(int,input().split())
print([int(L:=(a+b+((a+b)**2-4*(a*b-S))**0.5)/2),-1][int(L)<L])