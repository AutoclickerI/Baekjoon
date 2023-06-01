p,q=map(int,input().split())
P=[*range(p+1)]
A=M=0
def F(n):
 if P[n]-n:P[n]=F(P[n])
 return P[n]
S=sorted
for a,b,c in S([[*map(int,input().split())]for _ in[0]*q],key=lambda l:l[2]):
 a,b=S([F(a),F(b)])
 if a-b:A+=c;P[b]=a;M=max(M,c)
print(A-M)