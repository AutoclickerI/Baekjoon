n,d=map(int,input().split())
*l,=range(1,n+1)
l=*l[n-d:-1],*l[:n-d],l[-1]
for i in range(n//2):print(l[i],l[n+~i],sep='-')