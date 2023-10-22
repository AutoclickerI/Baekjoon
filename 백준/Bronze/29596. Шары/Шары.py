p,q=map(int,input().split())
r,s=map(int,input().split())
n=int(input())
(a,b),(c,d)=sorted([(p+q*n,q),(r+s*n,s)])
if p<r:
    print(a,b)
    print(c,d)
else:
    print(c,d)
    print(a,b)