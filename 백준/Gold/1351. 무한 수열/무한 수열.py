N,P,Q=map(int,input().split())
d={0:1}
def A(n):
 if~-(n in d):d[n]=A(n//P)+A(n//Q)
 return d[n]
print(A(N))