for i in[*open(b:=0)][1:]:
 B,s,*n=map(int,i.split());x=B-sum(n);b-=s*(s<=x);c=1
 while 1e4>=c<=x:c*=10
 b+=c//10
print(b)