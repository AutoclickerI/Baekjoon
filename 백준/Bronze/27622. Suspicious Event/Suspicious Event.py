d={0}
for i in[*open(s:=0)][1].split():
  if i[0]=='-':s+=1-(i[1:]in d);d-={i[1:]}
  else:d|={i}
print(s)