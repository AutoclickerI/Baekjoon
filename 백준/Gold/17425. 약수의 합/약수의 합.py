N=6**8
e=[i:=0]*N
while~i+N:
 e[j:=i+1]+=e[i];i=j
 while j<N:e[j]+=i;j+=i
for i in[*open(0)][1:]:print(e[int(i)])