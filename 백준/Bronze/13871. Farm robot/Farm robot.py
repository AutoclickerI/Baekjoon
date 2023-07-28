p=1
N,C,S=map(int,input().split())
a=1==S
for i in input().split():
    p+=(i=='1')*2-1
    a+=~-p%N+1==S
print(a)