p,q,r=sorted(map(int,input().split()))
print(1 if p+q==r else 2 if q*p==r else 3)