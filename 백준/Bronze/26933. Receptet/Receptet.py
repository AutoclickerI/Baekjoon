for i in[*open(a:=0)][1:]:p,q,r=map(int,i.split());a+=max(q-p,0)*r
print(a)