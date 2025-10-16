[N],*l=[[*map(int,i.split())]for i in open(0)]

m=1e9

for i in range(1,2**N):
    s=1
    b=0
    for c in range(N):
        if i&1<<c:
            s*=l[c][0]
            b+=l[c][1]
    m=min(m,abs(s-b))

print(m)