l=[1]*86400
for i in[*open(0)][1:]:v=int(i[:2])*3600+int(i[3:5])*60+int(i[6:]);l[v:v+40]=[0]*40
print(sum(l))