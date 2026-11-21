d={}
m=z=0
for i in[*open(0)][1].split():m=max(m,z+~d.get(i,z));d[i]=z;z+=1
print(m)