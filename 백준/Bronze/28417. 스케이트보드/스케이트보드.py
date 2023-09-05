a=[]
for i in[*open(0)][1:]:p,q,*l=map(int,i.split());a+=max(p,q)+sum(sorted(l)[3:]),
print(max(a))