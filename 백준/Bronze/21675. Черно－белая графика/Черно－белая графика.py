_,*p,s=open(0)
for i,j in zip(p,p[len(p)//2:]):print(*[s[int(x+y,2)]for x,y in zip(i,j[:-1])],sep='')