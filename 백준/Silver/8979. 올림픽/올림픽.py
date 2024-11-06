N,K=map(int,input().split())
l=[[*map(int,input().split())]for _ in[0]*N]
for i,p,q,r in l:
    if i==K:z=p,q,r
s=sorted((i,j,k)for _,i,j,k in l)[::-1]
print(s.index(z)+1)