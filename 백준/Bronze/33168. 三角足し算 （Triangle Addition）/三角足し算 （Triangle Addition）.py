l=[*open(0)][1].split()
while l:l=[int(i)+int(j)for i,j in zip(l,l[1:])];print(*l)