from bisect import*
_,*l=open(0)
while l:_,p,q,*l=l;q=sorted(map(int,q.split()));print(sum(bisect_left(q,int(i))for i in p.split()))