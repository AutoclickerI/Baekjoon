from itertools import*
R=range(N:=int(input()))
P=[*R]
A=0
def F(n):
 if P[n]-n:P[n]=F(P[n])
 return P[n]
S=sorted
for a,b,c in S([[a,d,((e-b)**2+(c-f)**2)**.5]for[a,b,c],[d,e,f]in combinations([[i,*map(float,input().split())]for i in R],2)],key=lambda l:l[2]):
 a,b=S([F(a),F(b)])
 if a-b:A+=c;P[b]=a
print(A)