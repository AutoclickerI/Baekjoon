l=sorted(int(i[:2])*3600+int(i[3:5])*60+int(i[6:])for i in[*open(0)][1:])
print(86360-sum(min(40,j-i)for i,j in zip(l,l[1:])))