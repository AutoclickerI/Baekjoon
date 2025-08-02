N,*l=map(int,open(0).read().split())
for i in range(N,f:=0,-1):f|=l[:N]==l[N:];l[k],l[i-1]=l[i-1],l[k:=l.index(max(l[:i]))]
print(f)