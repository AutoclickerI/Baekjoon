a=0
n,m=sorted(map(int,input().split()))
while n:a+=1;n,m=sorted([n,m-n])
print(a)