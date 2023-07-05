Z=range
P,*Q=open(0)
A=0
R,C,M=map(int,P.split())
B=[C*[(0,0,0)]for _ in[0]*R]
for i in Q:r,c,s,d,z=map(int,i.split());B[r-1][c-1]=z,s,d
for i in Z(C):
 for j in Z(R):
  if B[j][i][0]:A+=B[j][i][0];B[j][i]=0,0,0;break
 T=[C*[(0,0,0)]for _ in[0]*R]
 for K in Z(C):
  for l in Z(R):
   z,s,d=B[l][K]
   if d<3:
    l+=s*(2*d-3);l%=(2*R-2)
    if~-(0<=l<R):l=-l+2*R-2;d=3-d
    T[l][K]=max(T[l][K],(z,s,d))
   else:
    k=(K+s*(7-2*d))%(2*C-2)
    if~-(0<=k<C):k=-k+2*C-2;d=7-d
    T[l][k]=max(T[l][k],(z,s,d))
 B=T
print(A)