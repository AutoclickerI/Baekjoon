k,*l=open(0)
p,q=map(int,k.split())
P=[*range(p+1)]
A=0
def F(n):
 if P[n]-n:P[n]=F(P[n])
 return P[n]
S=sorted
for c,b,a in S([*map(int,i.split())][::-1]for i in l):
 a,b=S([F(a),F(b)])
 if a-b:A+=c;P[b]=a
print(A)