_,s,i=open(0)
U,D=map(int,i.split())
u,d=map(s.count,'12')
f=str.replace
print(['NO','YES\n'+f(f(f(f(f(s,*'3U',U-u),' ',''),*'2D'),*'1U'),*'3D')][u-U<1>d-D])