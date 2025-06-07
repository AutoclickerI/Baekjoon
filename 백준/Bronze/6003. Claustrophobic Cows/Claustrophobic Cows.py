_,*l=[eval(i.replace(' ','+1j*'))for i in open(0)]
N=len(l)
_,i=min((abs(l[i%N]-l[i//N])or 1e9,i)for i in range(N*N))
print(i//N+1,i%N+1)