n=int(input())
if n==3:print(-1)
elif n%2:print(*range(2,n-1),1,n,n-1,sep='\n')
else:print(*range(3,n+1),1,2,sep='\n')