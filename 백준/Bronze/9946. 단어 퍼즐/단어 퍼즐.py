*l,_,_=open(i:=0)
while l:a,b,*l=l;i+=1;print(f'Case {i}:',['different','same'][sorted(a)==sorted(b)])