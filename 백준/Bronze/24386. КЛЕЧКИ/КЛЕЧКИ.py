l=[' ']*101
m=100
M=0
for _ in[0]*3:
    s,e=map(int,input().split())
    l[s:e]=['1']*(e-s)
    m=min(m,e-s)
    M=max(M,e-s)
print(len(''.join(l).split()))
print(m,M)