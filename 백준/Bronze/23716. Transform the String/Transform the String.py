_,*l=open(T:=0,'rb')
while l:T+=1;(*a,_),(*b,_),*l=l;print(f'Case #{T}:',sum(min(min(z:=abs(i-j)%26,26-z)for j in b)for i in a))