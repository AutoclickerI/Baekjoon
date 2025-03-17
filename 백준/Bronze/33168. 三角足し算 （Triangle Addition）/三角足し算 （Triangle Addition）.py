*l,=map(int,[*open(0)][1].split())
while l:l=[i+j for i,j in zip(l,l[1:])];print(*l)