h,*p,s=open(0)
for i,j in zip(p,p[int(h.split()[1]):]):print(*[s[2*int(x)+int(y)]for x,y in zip(i,j[:-1])],sep='')