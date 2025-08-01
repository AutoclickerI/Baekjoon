a,b,n,w=map(int,input().split())
l=[(i,n-i)for i in range(1,n)if(n-i)*b+a*i==w]
print(*[-1]*(1!=len(l))or l[0])