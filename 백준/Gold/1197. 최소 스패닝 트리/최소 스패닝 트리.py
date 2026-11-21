import sys
sys.setrecursionlimit(9**9)
I=lambda:map(int,input().split())
p,q=I()
*P,=range(p+1)
A=0
def F(n):
 if P[n]-n:P[n]=F(P[n])
 return P[n]
S=sorted
for c,b,a in S([*I()][::-1]for _ in[0]*q):
 a,b=S([F(a),F(b)])
 if a-b:A+=c;P[b]=a
print(A)