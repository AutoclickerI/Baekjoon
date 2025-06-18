m=K=int(input())
for i in range(1,K+1):
    if K%i<1:m=min(m,max(i,K//i))
s=K//m
i=1
print(m+s)
for _ in range(m-s+1):
    print(i,i:=i+1)
for _ in range(s-1):
    print(i,i+1)
    print(i,i:=i+2)