n,*L=map(int,open(0).read().split())
print((m:=max(s:=L[1::2]))and L[::2][i:=s.index(m)]+20*i)