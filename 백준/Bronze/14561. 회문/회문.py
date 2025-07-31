for i in[*open(0)][1:]:
 A,n,*l=map(int,i.split())
 while A:l+=A%n,;A//=n
 print(+(l==l[::-1]))