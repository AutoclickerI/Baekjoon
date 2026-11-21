m=l=0
for i in[*open(0)][1:]:m=max(m,l:=l-eval(i.replace(*' -')))
print(m)