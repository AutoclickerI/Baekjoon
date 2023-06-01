R=range
P=[*R(n:=int(input()))]
X=[[i,*map(int,input().split())]for i in R(n)]
L=[]
S=sorted
for i in R(3):
 X=S(X,key=lambda l:l[i+1])
 for j in R(n-1):L+=[[X[j][0],X[j+1][0],X[j+1][i+1]-X[j][i+1]]]
A=0
def F(n):
 if P[n]-n:P[n]=F(P[n])
 return P[n]
for a,b,c in S(L,key=lambda l:l[2]):
 a,b=S([F(a),F(b)])
 if a-b:A+=c;P[b]=a
print(A)