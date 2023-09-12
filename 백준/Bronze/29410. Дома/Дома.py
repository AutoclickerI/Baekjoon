N,A,B=map(int,input().split())
ans=0
for _ in[0]*N:
    a,b=map(''.join(f'{i:b}'for i in[*map(int,input().split())][1:]).count,'01')
    ans+=a*A+b*B
print(ans)