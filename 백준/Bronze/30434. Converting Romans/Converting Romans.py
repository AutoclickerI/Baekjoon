d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
for s in[*open(0)][1:]:
    m=ans=0
    for i in s[::-1]:
        c=d.get(i,0)
        ans+=(1-2*(c<m))*c
        m=max(c,m)
    print(ans)