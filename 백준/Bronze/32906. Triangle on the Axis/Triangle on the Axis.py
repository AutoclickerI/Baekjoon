l=[]
h=0

for i in[*open(0)][1:]:
    s,e=map(int,i.split())
    if e:h=max(abs(e),h)
    else:l+=s,

l=l or[0]
print((max(l)-min(l))*h/2)