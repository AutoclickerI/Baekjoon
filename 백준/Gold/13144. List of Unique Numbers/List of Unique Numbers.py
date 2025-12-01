H={}
i=j=c=0
for v in[*open(0)][1].split():i+=1;j=max(j,H.get(v,0));H[v]=i;c+=i-j
print(c)