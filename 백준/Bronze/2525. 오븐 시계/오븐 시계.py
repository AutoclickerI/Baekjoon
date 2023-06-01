p,t=open(0)
m=int(p[2:])+int(t)
print((int(p[:2])+m//60)%24,m%60)