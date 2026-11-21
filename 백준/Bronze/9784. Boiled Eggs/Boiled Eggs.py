_,*l=[[*map(int,i.split())]for i in open(0)]
T=0
while l:T+=1;(n,p,q),a,*l=l;a.sort();print(f'Case {T}:',max(-~i*(i<p)*(sum(a[:i+1])<=q)for i in range(n)))