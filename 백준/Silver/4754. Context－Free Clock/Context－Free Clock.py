while 1:
 t,h,m,s=map(int,input().replace(*': ').split())
 if t<0:break
 t=((t*120-12*(y:=m*60+s)+(x:=h*3600+y))%43200//11+x)%86400;print(f'{t//3600:02d}:{t%3600//60:02d}:{t%60:02d}')