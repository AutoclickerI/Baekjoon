n,m,p=map(int,input().split())
print(sum((p-5<i%n+i//n<<1)*(n-i%n)*(m-i//n)for i in range(n*m)))