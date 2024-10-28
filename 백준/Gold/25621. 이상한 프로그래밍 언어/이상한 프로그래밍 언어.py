import sys
input=sys.stdin.readline
p,k=map(int,input().split())
m=(10**9+7)
for _ in[0]*p:
 p,q=input().split()
 P,Q=p[0],q[0]
 if P=='*':K=k*int(p[1:])
 else:K=k+int(p)
 if Q=='*':k*=int(q[1:])
 else:k+=int(q)
 k=max(k,K,0)%m**2
print(k%m)