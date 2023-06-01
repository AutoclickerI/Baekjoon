def count(n,k):
    num=0
    while n:
        n//=k
        num+=n
    return num
N,M=map(int,input().split())
p,q=count(N,5),count(N,2)
r,s=count(N-M,5),count(N-M,2)
t,u=count(M,5),count(M,2)
print(min(p-r-t,q-s-u))