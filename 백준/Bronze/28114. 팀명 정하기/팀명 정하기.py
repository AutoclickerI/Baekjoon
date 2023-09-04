l=[]
m=[]
for _ in[0]*3:
    p,q,r=input().split()
    l+=int(q)%100,
    m+=(-int(p),r),
print(*sorted(l),' ',*[j[0]for i,j in sorted(m)],sep='')