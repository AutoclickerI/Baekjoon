_,*l=open(0)
while l:n,p,q,*l=l;n=int(n);print(f'The maximum distance is {max(abs(i-j)*(p.split()[i]==q.split()[j])for i in range(n)for j in range(i,n))}\n')