*l,=map(int,[*open(0)][1].split())
print(min(abs(j-i)for i,j in zip(l,l[1:])))