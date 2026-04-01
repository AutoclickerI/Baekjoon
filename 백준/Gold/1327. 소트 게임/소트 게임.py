N,K,*v=map(int,open(0).read().split())

s={(*v,):0}

l=[(0,v)]

for c,v in l:
    for i in range(N-K+1):
        t=v[:]
        t[i:i+K]=t[i:i+K][::-1]
        z=*t,
        if z not in s:
            s[z]=c+1
            l+=(c+1,t),

print(s.get((*sorted(v),),-1))