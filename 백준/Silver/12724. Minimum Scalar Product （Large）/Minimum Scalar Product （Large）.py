f=lambda s:sorted(map(int,s.split()))
_,*l=open(i:=0)
while l:_,p,q,*l=l;i+=1;print(f'Case #{i}:',sum(x*y for x,y in zip(f(p),f(q)[::-1])))