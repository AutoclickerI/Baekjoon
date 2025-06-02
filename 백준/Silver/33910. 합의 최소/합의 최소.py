*l,n=map(int,[*open(0)][1].split())
print(n+sum(n:=min(n,i)for i in l[::-1]))