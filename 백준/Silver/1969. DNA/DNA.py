s=''
for i in[*zip(*[*open(c:=0)][1:])][:-1]:d=max('ACGT',key=i.count);s+=d;c+=len(i)-i.count(d)
print(s,c)