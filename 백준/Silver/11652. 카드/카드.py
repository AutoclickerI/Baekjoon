d={}
for i in[*open(0)][1:]:d[i]=d.get(i,0)+1
m=max(d.values())
print(min([int(i)for i in d if d[i]==m]))