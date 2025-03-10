[w],_,*l=[map(eval,i.split())for i in open(0)]
b=10
g=a=0
for x,G in l:g+=G;a+=G*x;b*=x>5.7
print(['IMPOSSIBLE',t:=max(0-(80*(g+w)-a*10)//-w,58)/10][t<=b])