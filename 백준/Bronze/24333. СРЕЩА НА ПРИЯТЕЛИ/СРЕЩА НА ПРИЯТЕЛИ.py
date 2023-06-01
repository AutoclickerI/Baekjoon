l1,r1,l2,r2,k=map(int,input().split())
p,q=max(l1,l2),min(r1,r2)
print(max(0,q-p-(p<=k<=q)+1))