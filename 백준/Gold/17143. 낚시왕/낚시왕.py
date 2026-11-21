Z=range
P,*Q=open(A:=0)
R,C,M=map(int,P.split())
B=[C*[X:=(0,)*3]for _ in[0]*R]
for i in Q:r,c,s,d,z=map(int,i.split());B[r-1][c-1]=z,s,d
for i in Z(C):
 for j in Z(R):
  if B[j][i][0]:A+=B[j][i][0];B[j][i]=X;break
 T=[C*[X]for _ in[0]*R]
 for K in Z(C):
  for l in Z(R):
   z,s,d=B[l][K]
   if d<3:
    l+=s*(2*d-3);l%=2*~-R
    if~-(0<=l<R):l=2*R-2-l;d=3-d
    T[l][K]=max(T[l][K],(z,s,d))
   else:
    k=(K+s*(7-2*d))%(2*C-2)
    if~-(0<=k<C):k=2*C-2-k;d=7-d
    T[l][k]=max(T[l][k],(z,s,d))
 B=T
print(A)