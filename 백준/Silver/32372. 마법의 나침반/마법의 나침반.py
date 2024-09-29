(n,m),*l=[map(int,i.split())for i in open(0)]
a,b=c,d=1,n
p,q=min,max
for x,y,k in l:exec("b=p(b,x-1);d=p(d,y-1) a=x;d=p(d,y-1) a=q(a,x+1);d=p(d,y-1) a=q(a,x+1);c=y a=q(a,x+1);c=q(c,y+1) a=x;c=q(c,y+1) b=p(b,x-1);c=q(c,y+1) b=p(b,x-1);c=y".split()[-k])
print(a,c)