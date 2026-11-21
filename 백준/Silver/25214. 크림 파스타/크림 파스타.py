m=1e9
for i in[*open(a:=0)][1].split():m=min(m,i:=int(i));print(a:=max(a,i-m))