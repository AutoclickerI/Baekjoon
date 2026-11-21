*l,=map(int,[*open(0)][1].split())
s=l.index(-1)
print(min(l[:s])+min(l[s+1:]))