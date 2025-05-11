s=1
n,d,*l=map(int,open(0).read().split())
while n:
 a,b=eval('l.pop(0)or 1e3,'*2);print('Scenario',s);s+=1
 for i in range(d):c,d,*l=l;print('Day',i+1,['OK','ALERT'][c+(c>=a)==n-d+(d<b)])
 n,d,*l=l