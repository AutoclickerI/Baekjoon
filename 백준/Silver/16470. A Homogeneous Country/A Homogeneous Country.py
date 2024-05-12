d={}
for i in open(0):d[i]=d.get(i,0)+1
c=d.values()
print(1-sum(V*V for V in c)/sum(c)**2)