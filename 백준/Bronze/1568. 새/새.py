cnt=0
n=int(input())
v=1
while n:
    if v>n:
        v=1
    n-=v
    v+=1
    cnt+=1
print(cnt)