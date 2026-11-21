p,q,r=map(int,input().split())
p,q=sorted([p,q])
v=(100-r)/p+r/q
print(100/v)