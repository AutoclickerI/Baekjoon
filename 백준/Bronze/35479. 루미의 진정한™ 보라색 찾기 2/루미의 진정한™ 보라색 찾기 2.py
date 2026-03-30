*l,=map(int,input().split())
s=max(l)
print(*[(s-i)/(s+1e-9)for i in l],1-s/255)