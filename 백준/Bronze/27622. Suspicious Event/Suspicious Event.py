d={0}
for i in[*open(s:=0)][1].split():
 if'0'>i:s+=d<d|{z:=i[1:]};d-={z}
 d|={i}
print(s)