g=1e9
print(-sum((g:=min(g-1,t:=int(i)))-t for i in[*open(0)][:0:-1]))