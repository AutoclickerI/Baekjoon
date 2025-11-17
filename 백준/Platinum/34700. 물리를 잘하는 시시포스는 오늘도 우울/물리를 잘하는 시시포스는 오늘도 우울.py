*l,=map(int,[*open(0)][1].split())
m=l.index(max(l))
print(sum(max(0,j-i)for i,j in zip(l[m+1:]+l,l[m:-1]+l[1:m+1])))