l=[1]
for _ in[0]*99:l+=sum(l[-2:]),
for i in[*open(0)][1:]:
    n=int(i)
    v=[]
    for i in l[::-1]:
        if i<=n:v+=i,;n-=i
    print(*v[::-1])