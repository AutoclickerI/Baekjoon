l=[x:=0]+[x:=x+int(i)for i in[*open(0)][1].split()]
print(min(l[-1]+i-2*j for i,j in enumerate(l)))