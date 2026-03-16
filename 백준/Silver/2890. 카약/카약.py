_,*s=open(0)
d={}
for i in s:
    for j,v in enumerate(i):
        if v.isdigit():
            d[v]=-j

s={v:i for i,v in enumerate(sorted({*d.values()}))}

for i in range(9):print(s[d[str(i+1)]]+1)