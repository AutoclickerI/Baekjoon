n=int(input())
a=0
for i in range(1,n-1):
    a+=(n-i)*(n-1-i)//2
print(a,3)