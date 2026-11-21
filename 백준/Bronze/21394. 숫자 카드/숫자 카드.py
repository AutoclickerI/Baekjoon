for i in[*open(0)][1:]:
 v,*l=[[],[]],;f=0
 for j,k in zip('123459789',i.split()):l+=j*int(k)
 for i in sorted(l)[::-1]:v[f]+=i;f^=1
 s,e=v;print(*s,*e[::-1])