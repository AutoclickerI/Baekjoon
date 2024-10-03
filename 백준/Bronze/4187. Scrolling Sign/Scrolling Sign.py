I=input
for _ in[0]*int(I()):
    n,m=map(int,I().split())
    s,r=I(),n
    for _ in[0]*~-m:
        t=I()
        for j in range(m,-1,-1):
            if s[n-j:]==t[:j]:r+=n-j;break
        s=t
    print(r)