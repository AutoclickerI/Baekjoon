N,S,M,*V=map(int,open(0).read().split())
l={S}
for i in V:l={v for j in l for v in(j-i,j+i)if 0<=v<=M}
print(max({*l,-1}))