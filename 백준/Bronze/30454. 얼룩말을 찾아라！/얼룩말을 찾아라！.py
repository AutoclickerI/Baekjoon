d={}
for i in[*open(0)][1:]:i=('0'+i).count('01');d[i]=d.get(i,0)+1
print(max(d),d[max(d)])