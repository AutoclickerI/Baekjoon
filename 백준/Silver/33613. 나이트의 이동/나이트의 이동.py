n,r,c=map(int,open(0).read().split())
if(n,r,c)==(3,2,2) or n==2:
    print(1)
else:
    print(n*n//2+(n+(n==3))*(r+c+1)%2)