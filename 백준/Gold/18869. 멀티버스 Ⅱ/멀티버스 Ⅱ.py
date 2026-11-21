D={}
for l in[*open(0)][1:]:l=l.split();d={j:i for i,j in enumerate(sorted({*l},key=int))};k=*(d[i]for i in l),;D[k]=D.get(k,0)+1
print(sum(D[v]*~-D[v]//2for v in D))