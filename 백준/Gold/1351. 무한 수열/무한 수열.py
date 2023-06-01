N,P,Q=map(int,input().split())
d={0:1}
def A(n):
    if d.get(n,0):return d[n]
    d[n]=A(n//P)+A(n//Q)
    return d[n]
print(A(N))