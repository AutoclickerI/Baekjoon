n,m,*l=map(int,open(0).read().split())
f=lambda i,j:n>i>-1<j<m and l[i*m+j]
t=lambda*l:sum(f(i+a,j+b)for i in range(n)for j in range(m)for a,b in l if f(i,j))//2
v=t((1,0),(-1,0),(0,1),(0,-1))
print(v,v+t((1,1),(1,-1),(-1,1),(-1,-1)))