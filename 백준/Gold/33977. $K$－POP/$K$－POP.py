m=K=int(input())
for i in range(1,K+1):
    if K%i<1:m=min(m,max(i,K//i))
s=K//m
i=1
print(m+s)
for v in range(m):print(i,i:=i+1)!=m-s<v!=print(i-1,i:=i+1)