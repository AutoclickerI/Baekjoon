d={}
for i,j in zip(*[map(int,i.split())for i in open(0)][1:]):d[i-j]=d.get(i-j,0)+1
print(max(d.values()))