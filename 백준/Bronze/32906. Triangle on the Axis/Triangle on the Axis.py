l=[]
for i in[*open(h:=0)][1:]:s,e=map(int,i.split());l+=[s]*(e==0);h=max(abs(e),h)
l=l or[0]
print((max(l)-min(l))*h/2)