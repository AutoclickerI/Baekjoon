T,D,M=map(int,input().split())
s=0
for _ in[0]*M:
    S=int(input())
    if S-s>=T:exit(print('Y'))
    s=S
print('YN'[D-s<T])