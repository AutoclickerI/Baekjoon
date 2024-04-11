*l,=map(int,[*open(0)][1].split())
print(sum(i>j for i,j in zip(l,l[1:])))