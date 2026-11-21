d={int(i):0for i in[*open(0)][1].split()}
for i in d:
 j=i
 while j<2e6:
  if(j:=j+i)in d:d[i]+=1;d[j]-=1
print(*d.values())