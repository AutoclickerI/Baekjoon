p,q,r=sorted(map(int,input().split()))
print(p+q+min(p+q-1,r))