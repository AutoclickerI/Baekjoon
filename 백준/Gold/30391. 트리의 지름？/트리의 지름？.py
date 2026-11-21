n,k=map(int,input().split())
for i in range(n-1):print(i+2,~-i//~-k*(i>0)+1)