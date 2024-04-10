while(i:=input())>'0':
 t,h,m,s=map(int,i.replace(*': ').split())
 t=((t*120-12*(y:=m*60+s)+(x:=h*3600+y))%43200//11+x)%86400;print('%02d:%02d:%02d'%(t//3600,t%3600//60,t%60))