g=[[]for _ in[0]*501]
for i in[*open(0)][2:]:a,b=map(int,i.split());g[a]+=b,;g[b]+=a,
f={1}
for i in g[1]:f|={i,*g[i]}
print(len(f)-1)