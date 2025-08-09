_,*l=open(0)
v=[0]*5
for i,j in zip(l,l[1:]):
    for x in zip(i,i[1:],j,j[1:-1]):
        if'#'not in x:
            v[x.count('X')]+=1
print(*v)