d,a,o,A,O=map(int,open(0).read().split())
print(100/(1+max(0,o-d*O)/max(1e-9,a-d*A)))