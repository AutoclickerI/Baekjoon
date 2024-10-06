a=p=0
for i,j in sorted([*map(int,i.split())]for i in[*open(0)][1:]):a+=i>p;p=i+j
print(a)