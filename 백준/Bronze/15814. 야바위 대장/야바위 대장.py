[*s,],_,*l=open(0)
for i in l:a,b=map(int,i.split());s[a],s[b]=s[b],s[a]
print(*s,sep='')