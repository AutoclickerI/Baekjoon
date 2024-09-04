*l,=map(int,[*open(0)][1].split())
m,M=min(l),max(l)
for i in l:print(max(M-i,i-m))