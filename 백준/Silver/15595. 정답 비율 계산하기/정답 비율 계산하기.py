a=0
d={}
z={'megalusion'}
for s in[*open(0)][1:]:
    _,i,n,*_=s.split()
    if i in z:
        continue
    if'4'==n:
        a+=d.get(i,0)
        z.add(i)
    else:
        d[i]=d.get(i,0)+1
z-={'megalusion'}
print(len(z)/(len(z)+a)*100 if z else 0)