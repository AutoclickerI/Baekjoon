d={}
for i in open(0):
 for j in i.split()[2:]:d[j]=d.get(j,0)+1
m=max(d.values())
print(-(1<len(s:=[i for i in d if d[i]==m]))or s[0])