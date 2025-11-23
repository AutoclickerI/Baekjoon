[N,L],*l=[[*map(int,i.split())]for i in open(0)]
z=r=0
for s,e in sorted(l):s=max(z,s);v=(s-e)//L;z=s-v*L;r-=v
print(r)