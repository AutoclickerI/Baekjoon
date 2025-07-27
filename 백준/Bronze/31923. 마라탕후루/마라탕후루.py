(n,p,q),A,B,*l=[map(int,i.split())for i in open(0)]
for a,b in zip(A,B):
 c=0
 while a-b:a+=p;b+=q;c+=1;99<c<exit(print('NO'))
 l+=c,
print('YES',*l)