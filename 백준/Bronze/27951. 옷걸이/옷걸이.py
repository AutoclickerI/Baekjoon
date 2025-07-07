n,*a,u,d=map(int,open(0).read().split())
for i in range(n):
 x=a[i]
 if x<3:a[i]=' UD'[x];u-=x<2;d-=x>1
if(u<0)|(d<0):exit(print('NO'))
for i in range(n):
 if a[i]==3:a[i]='DU'[u>0];u-=u>0
print('YES\n'+''.join(a))