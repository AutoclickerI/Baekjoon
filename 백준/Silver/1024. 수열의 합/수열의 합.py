p,q=map(int,input().split())
for n in range(q,101):
    s=(2*p//n-1-n)//2+1
    if 2*p==(2*s+n-1)*n and s>-1:print(*range(s,s+n));exit()
print(-1)