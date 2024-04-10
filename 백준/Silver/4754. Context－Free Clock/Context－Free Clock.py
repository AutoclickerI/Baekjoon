while(i:=input())>'0':
 t,h,m,s=map(int,i.replace(*': ').split())
 t=(t*120-12*(y:=m*60+s)+(x:=h*3600+y))%43200//11+x;print(f'{t//3600%24:02d}:{t%3600//60:02d}:{t%60:02d}')