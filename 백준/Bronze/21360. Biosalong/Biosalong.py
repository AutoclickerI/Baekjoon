l=[i for i,j in enumerate([*open(0)][1])if j=='.']
print(min(j-i-1for i,j in zip(l,l[1:])))