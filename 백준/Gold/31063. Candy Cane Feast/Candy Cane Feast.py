(N,M),l,z=[[*map(int,i.split())]for i in open(0)]

for e in z:
    s=0
    for i in range(N):
        if s<l[i]:
            s,l[i]=l[i],l[i]+min(l[i],e)-s
        if e<=s:
            break
    else:
        continue
print(*l)