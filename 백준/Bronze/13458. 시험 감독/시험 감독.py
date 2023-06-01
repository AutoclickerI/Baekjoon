input()
a=list(map(int,input().split()))
b,c=list(map(int,input().split()))
n=0
for k in a:
    if b>=k:
        n+=1
    else:
        k-=b
        n+=(k-1)//c+2
print(n)