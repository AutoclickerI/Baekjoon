n,d,*l=map(int,open(s:=0).read().split())
while n:a,b,*l=l;print('Scenario',s:=s+1);i=0;exec("c,d,*l=l;print('Day',i:=i+1,['OK','ALERT'][c+(c>=a>0)==n-d+1-(d>=b>0)]);"*d);n,d,*l=l