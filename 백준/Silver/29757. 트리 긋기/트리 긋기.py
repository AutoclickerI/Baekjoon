l=[i for _,_,i in sorted([*map(int,j.split()),k+1]for k,j in enumerate([*open(0)][1:]))]
for i,j in zip(l,l[1:]):print(i,j)