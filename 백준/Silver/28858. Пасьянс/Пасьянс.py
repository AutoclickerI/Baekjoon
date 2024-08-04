l=sorted(map(int,[*open(0)][1].split()))
print(sum(i-j&1for i,j in zip(l,l[1:]))+1)