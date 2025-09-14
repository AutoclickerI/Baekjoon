l=[]
for i in[*open(0)][1:]:print(s:=i[4:-1]*('R'<i)or l.pop(~(i.count('+')%len(l))));l+=s,