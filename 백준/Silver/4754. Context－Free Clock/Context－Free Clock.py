g=3600
while(i:=input())>'0':
 t,h,m,s=map(int,i.replace(*': ').split())
 t=(t*120-12*(y:=m*60+s)+(x:=h*g+y))%43200//11+x;print(f'{t//g%24:02d}:{t%g//60:02d}:{t%60:02d}')