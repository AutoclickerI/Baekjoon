A,B,C=map(int,input().split())
l=[(0,0,C)]
s={(0,0,C)}
for i,j,k in l:
    #AB
    nB=min(i+j,B)
    nA=i-nB+j
    t=[(nA,nB,k)]
    #BA
    nA=min(i+j,A)
    nB=j-nA+i
    t+=(nA,nB,k),
    #AC
    nC=min(i+k,C)
    nA=i-nC+k
    t+=(nA,j,nC),
    #CA
    nA=min(i+k,A)
    nC=k-nA+i
    t+=(nA,j,nC),
    #BC
    nC=min(j+k,C)
    nB=j-nC+k
    t+=(i,nB,nC),
    #CB
    nB=min(j+k,B)
    nC=k-nB+j
    t+=(i,nB,nC),
    for i in t:
        if i not in s:
            s|={i}
            l+=i,
print(*sorted({k for i,j,k in s if i==0}))