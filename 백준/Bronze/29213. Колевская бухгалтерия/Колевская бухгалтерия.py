a,b,c=map(int,input().split())
print(sum(b+i<a+j*2for i in range(c+1)for j in range(i+1)))