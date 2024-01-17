pa,ka,pb,kb,n=map(int,input().split())
m=(1e99,0,0)
for i in range(101):
    for j in range(101):
        if i*ka+j*kb>=n:
            m=min(m,(i*pa+j*pb,j,i))
print(*m[::-1])