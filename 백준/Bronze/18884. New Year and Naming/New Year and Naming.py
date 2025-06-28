v,s,t,_,*l=open(0)
for i in l:i=int(i)-1;print(s.split()[i%int(v[:2])]+t.split()[i%int(v[2:])])