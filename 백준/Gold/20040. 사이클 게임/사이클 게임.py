p,q=map(int,input().split())
P=[*range(p)]
A=[]
def F(n):
 n=int(n)
 if P[n]-n:P[n]=F(P[n])
 return P[n]
for i in range(q):
 a,b=sorted(map(F,input().split()))
 if a-b:P[b]=a
 else:A+=[i+1]
try:a=A[0]
except:a=0
print(a)