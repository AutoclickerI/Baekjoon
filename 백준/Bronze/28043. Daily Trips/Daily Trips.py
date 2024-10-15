s,*l=open(0)
n,h,w=map(int,s.split())
for a,_,b,_ in l:
 if w<1or'N'<a:w+=1;h-=1;a='Y'
 if h<1or'N'<b:w-=1;h+=1;b='Y'
 print(a,b)