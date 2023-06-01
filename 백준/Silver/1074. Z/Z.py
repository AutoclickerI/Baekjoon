N,r,c=map(int,input().split())
a=0
while N:
    N-=1
    a+=(r//2**N*2+c//2**N)*4**N
    r%=2**N
    c%=2**N
print(a)