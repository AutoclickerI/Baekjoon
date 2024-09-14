n,m=sorted(map(int,input().split()))
i=0
while n>=i*i//2<=m-i%2:i+=1
print(i-1)