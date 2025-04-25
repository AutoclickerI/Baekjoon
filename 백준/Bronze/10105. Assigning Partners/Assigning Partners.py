d={}
for i,j in zip(*[i.split()for i in open(0)][1:]):d[i]=j;d[j]=i
print('gboaodd'[any(i!=d[d[i]]or i==d[i]for i in d)::2])