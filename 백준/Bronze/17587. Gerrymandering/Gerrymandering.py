[p,d],*q=[map(int,i.split())for i in open(0)]
X=[0]*d
Y=X[:]
for d,a,b in q:X[d-1]+=a;Y[d-1]+=b
A=B=C=0
for a,b in zip(X,Y):k=a+b>>1;C+=a+b;x,y,z=[('B',a,b+~k),('A',a+~k,b)][a>b];print(x,y,z);A+=y;B+=z
print(abs(A-B)/C)