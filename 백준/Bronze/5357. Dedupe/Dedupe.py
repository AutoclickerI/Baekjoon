for i in[*open(0)][1:]:
 if i[-1]!='\n':i+='\n'
 for j in i:
  if i!=j:print(j,end='');i=j