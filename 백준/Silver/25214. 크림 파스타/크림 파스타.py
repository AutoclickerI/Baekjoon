a,m=0,1e9
for i in map(int,[*open(0)][1].split()):m=min(m,i);print(a:=max(a,i-m))