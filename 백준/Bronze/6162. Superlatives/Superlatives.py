for i in[*open(t:=0)][1:]:
 t+=1;p,q=map(int,i.split());s='no '*(p<=q)
 while(p:=p//5)>q:s+='mega '
 print(f"Data Set {t}:\n{s}drought\n")