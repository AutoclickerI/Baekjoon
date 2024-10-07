S=T=D=0
for i in open(0):
 x,*l=i.split();h,m,s=map(int,x.split(':'));D-=(T-(T:=h+m/60+s/3600))*S
 if l:S=int(l[0])
 else:print(x,f'{D:.2f} km')