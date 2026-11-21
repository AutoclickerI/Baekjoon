_,*l=[[*map(int,i.split())]for i in open(0)]
for x,y,r in l:print(sum(r+z>=abs(p-x+(q-y)*1j)for p,q,z in l)-1)