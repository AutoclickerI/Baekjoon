l=[]
for i in[*open(0)][1:]:n,m=map(int,i.split());l+=m//n,
print(min(l))