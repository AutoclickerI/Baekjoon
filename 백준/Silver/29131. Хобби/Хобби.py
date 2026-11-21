n=int(input())
l=sorted([[*map(int,input().split())],i]for i in range(n))
print(n//2)
for i in range(1,n,2):print(l[i-1][1]+1,l[i][1]+1)