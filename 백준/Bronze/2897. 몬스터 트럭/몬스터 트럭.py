_,*l=open(0)
v=[0]*5
for i,j in zip(l,l[1:]):
 for x in zip(i,i[1:],j,j[1:-1]):v[x.count('X')]+='#'<min(x)
print(*v)