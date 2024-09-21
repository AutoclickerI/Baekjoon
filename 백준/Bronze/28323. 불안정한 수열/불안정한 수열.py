*l,=map(int,[*open(0)][1].split())
print(1+sum(i+j&1for i,j in zip(l,l[1:])))