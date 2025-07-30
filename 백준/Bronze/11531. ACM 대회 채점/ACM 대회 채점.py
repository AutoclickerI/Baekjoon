p=c=0
d={}
while'0'<(s:=input()):t,v,q=s.split();f=q<'w';d[v]=d.get(v,0)+20;p+=(int(t)+d[v]-20)*f;c+=f
print(c,p)