a,b,*l=sorted([*open(v:=0)][1:],key=lambda i:-int(i[4:]))
while a[0]==b[0]==l[v][0]:v+=1
for i in a,b,l[v]:print(i[:4])