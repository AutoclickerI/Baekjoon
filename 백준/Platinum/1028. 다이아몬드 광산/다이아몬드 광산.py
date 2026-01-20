R,C=map(int,input().split())
b=[input()for _ in[0]*R]
lu=[[+i for i in map('1'.__eq__,b[0])]]
ru=lu[:]
for i in b[1:]:
    lu+=[(p=='1')*(q+1)for p,q in zip(i,[0]+lu[-1])],
    ru+=[(p=='1')*(q+1)for p,q in zip(i,ru[-1][1:]+[0])],
ld=[[+i for i in map('1'.__eq__,b[-1])]]
rd=lu[:]
for i in b[:-1][::-1]:
    ld+=[(p=='1')*(q+1)for p,q in zip(i,[0]+ld[-1])],
    rd+=[(p=='1')*(q+1)for p,q in zip(i,rd[-1][1:]+[0])],  
ld=ld[::-1]
rd=rd[::-1]

m=0
for y in range(R):
    for x in range(C):
        k=min(ld[y][x],rd[y][x])
        for rk in range(m,k):
            if rd[y+rk][x-rk]>rk<ld[y+rk][x+rk]:
                m=max(m,rk+1)
print(m)