l=sorted([*map(int,i.split())]for i in[*open(0)][1:])
m=1e9
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i][1]>l[j][1]:
            m=min(m,(l[j][0]-l[i][0])/(l[i][1]-l[j][1]))
print(m)