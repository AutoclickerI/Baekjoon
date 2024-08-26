l=sorted(map(int,[*open(0)][1:]))
print(min(j-i for i,j in zip(l,l[2:]))/2)