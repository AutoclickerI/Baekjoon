T=input
for _ in[0]*int(T()):
 M=int(T().split()[1]);*L,=map(int,T().split())
 if 3in L:L=L[::-1]
 I=L.index([2,3][3in L])+1
 while len(L)<1e4:L=L+(L[:-1])[::-1]
 print(sum([L[i]<1for i in range(I,I+M)]))