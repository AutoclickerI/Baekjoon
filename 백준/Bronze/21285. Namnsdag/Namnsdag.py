z,_,*l=open(c:=0)
for s in l:c+=1;len(s)==len(z)>sum(map(str.__ne__,s,z))<2<exit(print(c))