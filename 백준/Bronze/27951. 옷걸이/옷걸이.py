_,s,i=open(0)
U,D=map(int,i.split())

u,d,b=map(s.count,'123')

s=s.translate({49:85,50:68})

s=s.split()

if U<u or D<d:
    print('NO')
else:
    print('YES')
    c=U-u
    i=0
    while c:
        if s[i]=='3':s[i]='U';c-=1
        i+=1
    print(''.join(s).replace(*'3D'))