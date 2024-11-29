A,B,C,D,E,F,G,H=map(int,input().split())
ans=0
for m in range(1,H):
    l=H-m
    for h in range(1,D):
        d=D-h
        if len({m,l,d,h})<4:
            continue
        for k in range(1,14):
            if k in(m,l,d,h):
                continue
            for g in range(1,C-k):
                c=C-g-k
                if len({g,m,l,h,d,k,c})<7:
                    continue
                for j in range(1,G-k):
                    i=G-j-k
                    if len({m,l,h,d,k,c,g,j,i})<9:
                        continue
                    for f in range(1,min(B-j-m,F-g-h)):
                        b=B-f-j-m
                        e=F-f-g-h
                        a=E-b-c-d
                        if A-e-i-l==a and 0<a and len({a,b,c,d,e,f,g,h,i,j,k,l,m})==13:
                            ans+=1
print(ans)