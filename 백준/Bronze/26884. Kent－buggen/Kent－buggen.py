d={}
for i in open(0):d[i]=d.get(i,0)+1
print(sum(d[i]>1for i in d))