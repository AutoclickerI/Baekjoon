n,*a=map(int,open(0).read().split())
f,d=a.index,divmod
(p,q),(r,s)=map(sorted,zip(d(f(2),n),d(f(5),n)))
print(+(((p-q)**2+(r-s)**2>24)*sum(a[i*n+r:i*n-~s].count(1)for i in range(p,q+1))>2))