(n,t,a),*l=[map(int,i.split())for i in open(0)]
for m,*l in l:
 n=b=m=s=0
 for i in l:
  n+=1;s+=i;m=max(i,m)
  if s>t:
   if b or s-m+a>t:n-=1;break
   b=1;s+=a-m
 print(n)