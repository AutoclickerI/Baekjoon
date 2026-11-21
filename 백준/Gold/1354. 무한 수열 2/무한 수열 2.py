d={}
def A(n):
    if n<1:return 1
    if n in d:return d[n]
    d[n]=A(n//P-X)+A(n//Q-Y)
    return d[n]

N,P,Q,X,Y=map(int,input().split())
print(A(N))