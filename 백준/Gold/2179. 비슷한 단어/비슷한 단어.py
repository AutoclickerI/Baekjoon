r=-1
d={}
idx=0
for s in[*open(0)][1:]:
    idx+=1
    for i in range(len(s)):
        ps=s[:i]
        if ps in d:
            if r<len(ps):
                a=[(d[ps][0],idx,d[ps][1],s)]
                r=len(ps)
            if r==len(ps):
                a+=(d[ps][0],idx,d[ps][1],s),
        if ps not in d:
            d[ps]=idx,s
print(*min(a)[2:],sep='')