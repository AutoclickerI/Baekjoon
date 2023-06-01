N,P=map(int,input().split())
a=1
for i in range(N):
    a*=i+1
    a%=P
print(a)