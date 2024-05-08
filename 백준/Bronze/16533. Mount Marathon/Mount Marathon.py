*l,=map(int,[*open(0)][1].split())
print(1+sum(x<y for x,y in zip(l,l[1:])))