from functools import*

def suffix_array(s):
    n=len(s)
    *sa,=range(n)
    g=[ord(c)-97 for c in s]+[-1]
    tg=[0]*n
    t=1

    while t<=n:
        def compare(a,b):
            if g[a]==g[b]:
                return -1 if g[a+t]<g[b+t] else g[a+t]>g[b+t]
            return -1 if g[a]<g[b] else 1

        sa.sort(key=cmp_to_key(compare))
        tg[sa[0]]=0

        for i in range(1,n):
            if compare(sa[i-1],sa[i])<0:
                tg[sa[i]]=tg[sa[i-1]]+1
            else:
                tg[sa[i]]=tg[sa[i-1]]

        g=tg+[-1]
        t*=2

    return sa

def lcp_array(s,sa):
    n=len(s)
    lcp=[0]*n
    rk=[0]*n

    for i in range(n):
        rk[sa[i]]=i

    l=0
    for i in range(n):
        if rk[i]:
            j=sa[rk[i]-1]
            while i+l<n and j+l<n and s[i+l]==s[j+l]:
                l+=1
            lcp[rk[i]]=l
            if l:
                l-=1

    return lcp

s=input()
sa=suffix_array(s)
lcp=lcp_array(s,sa)

print(*[i+1 for i in sa])
print('x',*lcp[1:])