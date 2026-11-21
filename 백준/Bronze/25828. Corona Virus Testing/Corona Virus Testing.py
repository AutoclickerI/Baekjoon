p,q,r=map(int,input().split())
m=p*q
n=r*q+p
print(1if m<n else 2if m-n else 0)