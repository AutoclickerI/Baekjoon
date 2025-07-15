mp=lambda d:(m:=-int(((1+8*d)**.5-1)//-2),d-~-m*m//2)
P=lambda x:~x*x//-2
Q=lambda x:~-~x*~x*x//6
A,B=map(int,input().split())
mA,pA=mp(A)
mB,pB=mp(B)
print(P(pB)-P(pA-1)+(P(mA)+Q(mB-1)-Q(mA))*(mA<mB))