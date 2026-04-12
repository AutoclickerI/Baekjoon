_,s,*l=map(str.split,open(0))

d={}
for i in l:
    for c in i:d[c]=d.get(c,0)+1

l=sorted((-d.get(i,0),i)for i in s)
for s,i in l:
    print(i,-s)