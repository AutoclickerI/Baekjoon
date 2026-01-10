s,*l=open(0)

dl=[[1]+[0]*len(s)]
al=[[1]+[0]*len(s)]
for d,a in zip(*l):
    dt=dl[-1][:]
    at=al[-1][:]
    for i in range(len(s)):
        if s[i]==d:
            dt[i+1]+=al[-1][i]
        if s[i]==a:
            at[i+1]+=dl[-1][i]
    dl+=dt,
    al+=at,
print(dl[-1][-1]+al[-1][-1])