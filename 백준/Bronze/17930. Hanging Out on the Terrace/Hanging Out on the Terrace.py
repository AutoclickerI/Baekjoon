L,_,*l=open(0).read().split()
c=v=0
while l:p,q,*l=l;q=int(q)*((p<'l')*2-1);f=int(L)<c+q;v+=f;c+=q-f*q
print(v)