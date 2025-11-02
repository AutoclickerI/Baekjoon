s=''
for i in[*zip(*[*open(c:=0)][1:])][:-1]:c+=len(i)-i.count(d:=max('ACGT',key=i.count));s+=d
print(s,c)