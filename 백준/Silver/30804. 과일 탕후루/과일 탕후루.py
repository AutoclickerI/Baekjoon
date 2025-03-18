l=[-1]*10
o=i=0
for v in[*open(0)][1][::2]:l[int(v)]=i;o=max(o,i-sorted(l)[-3]);i+=1
print(o)