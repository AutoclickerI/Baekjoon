d={0}
for i in[*open(s:=0)][1].split():
  if'0'>i:s+=1-({i[1:]}<=d);d-={i[1:]}
  d|={i}
print(s)