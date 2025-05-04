_,*l=open(i:=0)
while l:_,p,q,*l=l;i+=1;print(f'Case {i}:',sum(map(str.__ne__,p,q)))